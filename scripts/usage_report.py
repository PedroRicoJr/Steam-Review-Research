# Cost per firing and per unit from usage_from_log.py output (DIR/usage.json) plus DIR/commits.txt from git log --format="%aI|%s"; size bound: a few thousand calls.
# Usage: python scripts/usage_report.py DIR [firings | since ISO-TIME]
import json, sys, datetime as dt
S=sys.argv[1]
U=json.load(open(S+"/usage.json")); r=U["rates"]
def T(s): return dt.datetime.fromisoformat(s.replace("Z","+00:00"))
calls=[(T(c[0]), r[0]*c[1]+r[1]*c[2]+r[2]*c[3]+r[3]*c[4], c) for c in U["calls"]]
commits=sorted((T(l.split("|",1)[0]), l.split("|",1)[1].strip()) for l in open(S+"/commits.txt"))
prompts=[(T(p[0]),p[1]) for p in U["prompts"]]
def window(a,b):
    cs=[c for c in calls if a<=c[0]<b]; return cs
# firing windows: from a prompt to the next prompt
rows=[]
for i,(t,txt) in enumerate(prompts):
    end=prompts[i+1][0] if i+1<len(prompts) else dt.datetime.max.replace(tzinfo=dt.timezone.utc)
    cs=window(t,end); units=[c for c in commits if t<=c[0]<end]
    if not cs: continue
    cost=sum(c[1] for c in cs); main=[c for c in cs if not c[2][5]]
    rows.append((t,txt,len(units),cost,len(cs),sum(c[2][3] for c in cs),sum(c[2][2] for c in cs)))
mode=sys.argv[2] if len(sys.argv)>2 else "firings"
if mode=="firings":
    for t,txt,n,cost,k,cr,out in rows:
        if t>=T("2026-10-05T00:00:00Z"):
            print("%s  units %2d  $%6.2f  per unit %s  calls %4d  %-40s"%(t.strftime("%m-%d %H:%M"),n,cost,("$%.2f"%(cost/n)) if n else "   -  ",k,txt[:40]))
elif mode=="since":
    a=T(sys.argv[3]); cs=window(a,dt.datetime.max.replace(tzinfo=dt.timezone.utc))
    tot=sum(c[1] for c in cs); n=[c for c in commits if c[0]>=a]
    inp=sum(c[2][1] for c in cs); out=sum(c[2][2] for c in cs); cr=sum(c[2][3] for c in cs); cw=sum(c[2][4] for c in cs)
    print("since",a,": calls",len(cs),"commits",len(n),"cost $%.2f"%tot)
    print("  input %d  output %d  cache read %d  cache write %d"%(inp,out,cr,cw))
    print("  cost split: input $%.2f output $%.2f cache read $%.2f cache write $%.2f"%(r[0]*inp,r[1]*out,r[2]*cr,r[3]*cw))
    print("  subagent cost $%.2f"%sum(c[1] for c in cs if c[2][5]))
    # this chat since the last loop commit
    last=max(c[0] for c in commits if "batch 23" in c[1])
    print("  after the last unit (chat with Rico) $%.2f"%sum(c[1] for c in cs if c[0]>last))
