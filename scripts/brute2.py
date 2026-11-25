import numpy as np
from functools import lru_cache
N=40
# enumerate: multiset of parts ≡2 mod 4 (non-overlined, any multiplicity), odd parts: each odd j has state 0, j, jbar (1 way each), or j+jbar (1 way)
# => per odd part j: weight options: 0 (1 way), j (2 ways: overlined or not), 2j (1 way)
def parts2(n,maxp):  # partitions of n into parts ≡2 mod 4, return list of counts by number of parts m
    res={}
    def rec(n,maxp,m):
        if n==0: res[m]=res.get(m,0)+1; return
        for p in range(min(n,maxp),1,-1):
            if p%4==2: rec(n-p,p,m+1)
    rec(n,maxp,0); return res
def odd_ways(n,bound):  # odd parts < bound, generating weights 1+2x^j+x^{2j}
    c=[0]*(n+1); c[0]=1
    for j in range(1,min(bound,n+1),2):
        d=c[:]
        for i in range(n+1):
            if i>=j: d[i]+=2*c[i-j]
            if i>=2*j: d[i]+=c[i-2*j]
        c=d
    return c
out=[]
for n in range(N):
    tot=0
    for a in range(0,n+1):
        for m,cnt in parts2(a,a).items():
            tot+=cnt*odd_ways(n-a,2*m)[n-a]
    out.append(tot)
S=np.load('op2_40.npy') if False else None
print(out)
