# Exact token use per API call from a Claude Code session log; size bound: reads one log (~100 MB) line by line.
# Usage: python scripts/usage_from_log.py OUT.json [SESSION_LOG_DIR_WITHOUT_.jsonl]
import json, glob, sys
import numpy as np
D=sys.argv[2] if len(sys.argv)>2 else "/root/.claude/projects/-home-user-Steam-Review-Research/387dd957-c864-5e66-9102-a7a671354378"
calls={}; snaps=[]; prompts=[]
def scan(path, sub):
    for line in open(path):
        try: d=json.loads(line)
        except Exception: continue
        t=d.get("type")
        if t=="assistant":
            m=d.get("message",{}); u=m.get("usage")
            if u and m.get("id"):
                calls[(sub,m["id"])]=(d["timestamp"],u,sub)
        elif t=="cost-state" and not sub:
            mu=d.get("modelUsage",{})
            if len(mu)==1:
                v=list(mu.values())[0]; snaps.append((v["inputTokens"],v["outputTokens"],v["cacheReadInputTokens"],v["cacheCreationInputTokens"],d["totalCostUSD"]))
        elif t=="user" and not sub:
            c=d.get("message",{}).get("content")
            txt=c if isinstance(c,str) else " ".join(x.get("text","") for x in c if isinstance(x,dict) and x.get("type")=="text") if isinstance(c,list) else ""
            if txt and not d.get("isMeta") and not any(isinstance(x,dict) and x.get("type")=="tool_result" for x in (c if isinstance(c,list) else [])):
                prompts.append((d["timestamp"], txt[:60].replace("\n"," ")))
scan(D+".jsonl", "")
for f in glob.glob(D+"/subagents/*.jsonl"): scan(f, f.split("/")[-1][:12])
A=np.array([s[:4] for s in snaps],float); y=np.array([s[4] for s in snaps])
rates,res,_,_=np.linalg.lstsq(A,y,rcond=None)
json.dump({"rates":rates.tolist(),
           "calls":sorted([(ts,u.get("input_tokens",0),u.get("output_tokens",0),u.get("cache_read_input_tokens",0),u.get("cache_creation_input_tokens",0),sub) for (sub,_),(ts,u,sub) in calls.items()]),
           "prompts":sorted(prompts)}, open(sys.argv[1],"w"))
print("calls",len(calls),"snapshots",len(snaps),"rates per million tokens (input, output, cache read, cache write):",[round(r*1e6,3) for r in rates])
fit=A@rates; print("worst fit error on a snapshot: $%.4f"%max(abs(fit-y)))
