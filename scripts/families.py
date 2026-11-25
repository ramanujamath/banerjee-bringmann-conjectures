import numpy as np
from collections import defaultdict
found=[tuple(x) for x in np.load('found.npy')]
val=np.load('op1_4m_mod4.npy')
def fac(n):
    f={};d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
byA=defaultdict(list)
for A,B in found: byA[A].append(B)
for A in sorted(byA):
    Bs=byA[A]; f=fac(A)
    # describe residues of N=8m+1 mod primes
    desc=[]
    for p in f:
        if p in (2,): continue
        Ns=sorted(set((8*B+1)%(p**f[p]) for B in Bs))
        desc.append((p,f[p],len(Ns),Ns[:6]))
    print(A,f,len(Bs),desc)
