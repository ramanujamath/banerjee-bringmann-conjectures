import numpy as np, math
val=np.load('op1_4m_mod4.npy').astype(np.int64)
LIM=200000
sieve=np.ones(LIM,dtype=bool); sieve[:2]=False
for i in range(2,int(LIM**.5)+1):
    if sieve[i]: sieve[i*i::i]=False
def rep(p,k,cond=None):
    for y in range(1,int(math.isqrt(p//k))+1):
        x2=p-k*y*y; x=math.isqrt(x2)
        if x*x==x2 and (cond is None or cond(y)): return 1
    return 0
bad=0; cnt=0; fam=[]
for p in np.nonzero(sieve)[0]:
    p=int(p)
    if p%8!=1: continue
    eps_actual=int(val[(p-1)//8])//2 % 2
    assert val[(p-1)//8] in (0,2)
    if p%24==17: eps=rep(p,32)
    else: eps=(1+rep(p,32)+rep(p,72)+rep(p,24,lambda y:y%2==1))%2
    cnt+=1; bad+= eps!=eps_actual
    if eps==0 and p%24==1 and len(fam)<15: fam.append(p)
print("primes p≡1 mod 8 below",LIM,":",cnt," rule mismatches:",bad)
print("first p≡1 mod 24 giving families:",fam)
