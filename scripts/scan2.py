import itertools
from lib import *
N=1500
ks=[1,2,3,4,6,8,12]
seen={}
for es in itertools.product([-2,-1,0,1,2],repeat=3):
  for kk in itertools.combinations(ks,3):
    ex={k:e for k,e in zip(kk,es) if e}
    key=tuple(sorted(ex.items()))
    if not ex or key in seen or 1 not in ex or ex[1]>=0: continue
    seen[key]=1
    c=series(ex,N)
    if any(v<0 for v in c): continue   # keep combinatorial (nonneg) ones
    for m in [5,7,11,13]:
        nz=sum(1 for v in c[100:] if v%m)/len(c[100:])
        if nz<0.5: continue   # skip lacunary-mod-m cases
        r=congr(c,m)
        if r: print(key,m,r,flush=True)
