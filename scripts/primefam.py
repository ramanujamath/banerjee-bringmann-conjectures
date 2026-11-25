import numpy as np
val=np.load('op1_4m_mod4.npy').astype(np.int64); M=len(val)
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
def leg(a,p): a%=p; return 0 if a==0 else (1 if pow(a,(p-1)//2,p)==1 else -1)
m=np.arange(M); N=8*m+1
res=[]
for p in [q for q in range(5,400) if isprime(q)]:
    mask=(N%p==0)&((N//p)%p!=0)
    allz=bool(np.all(val[mask]==0)); frac=float(np.mean(val[mask]==0))
    res.append((p,p%24,leg(-1,p),leg(-2,p),leg(-6,p),allz,round(frac,3)))
for r in res: print(r)
