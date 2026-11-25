import numpy as np, math
val=np.load('op1_4m_mod4.npy').astype(np.int64)
LIM=200000
sieve=np.ones(LIM,dtype=bool); sieve[:2]=False
for i in range(2,int(LIM**.5)+1):
    if sieve[i]: sieve[i*i::i]=False
def rep(p,k):
    return any(math.isqrt(p-k*y*y)**2==p-k*y*y for y in range(1,int(math.isqrt(p//k))+1))
all72=True; bad=0; n=0
for p in np.nonzero(sieve)[0]:
    p=int(p)
    if p%24!=1: continue
    n+=1
    all72 &= rep(p,72)
    eps=int(val[(p-1)//8])//2%2
    bad += eps != (0 if rep(p,32)!=rep(p,96) else 1)
print("p≡1 mod 24 below",LIM,":",n,"| all represented by x^2+72y^2:",all72,"| simplified-rule mismatches:",bad)
# class numbers by counting reduced forms
def h(D):
    c=0;a=1
    while 3*a*a<=-D:
        for b in range(-a+1,a+1):
            if (b*b-D)%(4*a)==0:
                cc=(b*b-D)//(4*a)
                if cc>=a and not (b<0 and a==cc) and math.gcd(math.gcd(a,abs(b)),cc)==1: c+=1
        a+=1
    return c
print({D:h(D) for D in (-128,-288,-96,-384,-576)})
