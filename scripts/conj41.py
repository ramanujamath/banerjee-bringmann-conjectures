import numpy as np
S=np.load('op1_40000.npy'); N=len(S)
def leg(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1
primes=[p for p in range(3,200) if all(p%d for d in range(2,int(p**.5)+1))]
bad=0
for p in primes:
    for k in range(p):
        vals=S[4*k::4*p]
        allEven=bool(np.all(vals%2==0))
        pred = leg(8*k+1,p)==-1
        if allEven!=pred: bad+=1; print("MISMATCH",p,k,allEven,leg(8*k+1,p),len(vals))
print("primes up to",primes[-1],"mismatches:",bad)
# odd values: structure of op(4m) parity
m=np.arange(N//4); odd=m[(S[4*m]%2)==1]
print("first m with op(4m) odd:",odd[:40].tolist())
import math
print("are all 8m+1 squares?", all(math.isqrt(8*x+1)**2==8*x+1 for x in odd))
print("parity of op(4m+2):", np.unique(S[2::4]%2))
