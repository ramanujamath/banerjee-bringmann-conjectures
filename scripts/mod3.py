import numpy as np, math
from collections import Counter
val=np.load('op1_4m_mod4.npy').astype(np.int64)
for r in range(3):
    v=val[r::3]; print("m≡%d mod 3: distribution"%r, Counter(v[:300000].tolist()))
# for m≡2 mod 3: where nonzero?
nz=[m for m in range(2,3000,3) if val[m]!=0]
print("m≡2 mod3 nonzero:", nz[:30])
print("N=8m+1:", [8*m+1 for m in nz[:30]])
def fac(n):
    f={};d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
print([fac(8*m+1) for m in nz[:30]])
