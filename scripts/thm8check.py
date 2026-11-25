import numpy as np, math
val=np.load('op1_4m_mod4.npy').astype(np.int64); Mx=len(val)
N=8*np.arange(Mx,dtype=np.int64)+1
isq=np.zeros(Mx,dtype=bool)
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
tot=bad=0
for p in [q for q in range(17,5000) if q%8==1 and isprime(q)]:
    eps=int(val[(p-1)//8])//2%2
    mask=(N%p==0)&((N//p)%p!=0)
    cof=N[mask]//p; r=np.sqrt(cof).astype(np.int64)
    sq=(r*r==cof)|((r+1)*(r+1)==cof)
    pred=2*eps*sq
    tot+=int(mask.sum()); bad+=int(np.sum((val[mask]-pred)%4!=0))
print("cases:",tot,"mismatches:",bad)
