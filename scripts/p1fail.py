import numpy as np, math
from collections import Counter
val=np.load('op1_4m_mod4.npy').astype(np.int64); Mx=len(val)
N=8*np.arange(Mx)+1
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
for p in [q for q in range(5,700) if isprime(q) and q%24 in (1,17)]:
    mask=(N%p==0)&((N//p)%p!=0)
    fails=np.nonzero(mask & (val!=0))[0]
    cof=N[fails]//p
    allsq=all(math.isqrt(int(c))**2==int(c) for c in cof)
    # at N=p*k^2 values by k mod 3
    ks=[k for k in range(1,int(math.isqrt((8*Mx)//p))+1,2) if k%p and (p*k*k)%8==1]
    vals=Counter((k%3, int(val[(p*k*k-1)//8])) for k in ks if (p*k*k-1)//8<Mx)
    rep32=any(math.isqrt(p-32*y*y)**2==p-32*y*y for y in range(1,int(math.isqrt(p//32))+1))
    print(p,p%24,"x2+32y2" if rep32 else "-", "fails:",len(fails),"all at N=p*k^2:",allsq, dict(vals))
