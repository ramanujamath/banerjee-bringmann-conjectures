import numpy as np, math
val=np.load('op1_4m_mod4.npy').astype(np.int64)
L=20000   # in Q-exponent E; m=3E
Nmax=24*L+2
def ser(exps):
    c=np.zeros(L,dtype=np.int64)
    for e in exps:
        if 0<=e<L: c[e]^=1
    return c
K=range(-300,301)
P=ser([k*(3*k-1)//2 for k in K])
psi=lambda s: ser([s*n*(n+1)//2 for n in range(0,400)])
u=lambda s: ser([s*k*(3*k+2) for k in K])
X=lambda s: ser([s*y*y for y in range(1,400)])
mul=lambda a,b: np.convolve(a,b)[:L]%2
sh=lambda a,k: np.concatenate([np.zeros(k,dtype=np.int64),a[:L-k]])
T1=mul(P,X(6)); T2=mul(P,X(12)); T3=sh(mul(psi(3),u(2)),1)
T4a=sh(mul(P,psi(8)),1); T4b=sh(mul(P,psi(24)),3)
# also the un-reduced B term: Q P psi(Q^6) psi(Q^2)
T4full=sh(mul(P,mul(psi(6),psi(2))),1)
print("T4 reduction ok:", np.array_equal(T4full,(T4a+T4b)%2))
E0=(T1+T2+T3+T4full)%2
r32=np.zeros(L,dtype=np.int64)
for E in range(L):
    N=24*E+1; cnt=0
    for y in range(-int(math.isqrt(N//32))-1,int(math.isqrt(N//32))+2):
        x2=N-32*y*y
        if x2>=0:
            x=math.isqrt(x2)
            if x*x==x2: cnt+= 2 if x>0 else 1
    r32[E]=cnt
actual=val[0:3*L:3]
pred=(r32//2+2*E0)%4
print("direct-theta class 0 prediction matches:", np.array_equal(pred,actual))
