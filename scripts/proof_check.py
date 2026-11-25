# exact integer power-series checks (python ints), N terms
N=1500
def mul(a,b):
    c=[0]*N
    for i,x in enumerate(a):
        if x:
            for j in range(N-i): c[i+j]+=x*b[j]
    return c
def inv(a):  # a[0]=1
    b=[0]*N; b[0]=1
    for n in range(1,N): b[n]=-sum(a[k]*b[n-k] for k in range(1,n+1))
    return b
def poch(sign, start, step, count):  # prod_{j<count} (1 + sign q^{start+j*step}), count may be None->infinite
    c=[0]*N; c[0]=1; j=0
    while (count is None or j<count):
        e=start+j*step
        if e>=N: break
        for i in range(N-1,e-1,-1): c[i]+=sign*c[i-e]
        j+=1
    return c
def shift(a,s): return [0]*s+a[:N-s]
def sub(a,f): return [a[i*f] if i*f<N else 0 for i in range(N)]   # not used
# nu(q) = sum q^{n(n+1)} / (-q;q^2)_{n+1};  omega(q)= sum q^{2n(n+1)}/(q;q^2)_{n+1}^2
nu=[0]*N; om=[0]*N; n=0
while n*(n+1)<N:
    t=shift(inv(poch(+1,1,2,n+1)),n*(n+1)); nu=[x+y for x,y in zip(nu,t)]
    if 2*n*(n+1)<N:
        d=poch(-1,1,2,n+1); t=shift(inv(mul(d,d)),2*n*(n+1)); om=[x+y for x,y in zip(om,t)]
    n+=1
# Identity: nu(-q) = q*omega(q^2) + (q^4;q^4)^3/(q^2;q^2)^2
lhs=[(-1)**i*x for i,x in enumerate(nu)]
om2=[0]*N
for i in range(N):
    if 2*i+1<N: om2[2*i+1]=om[i]
f4=poch(-1,4,4,None); f2=poch(-1,2,2,None)
rhs=[a+b for a,b in zip(om2, mul(mul(mul(f4,f4),f4), inv(mul(f2,f2))))]
print("nu identity exact:", lhs==rhs)
# Mod-2 claim: sum_n op(2n) q^n == nu(q)/(q^2;q^2) mod 2
import numpy as np
S=np.load('op1_40000.npy')
F=mul(nu, inv(f2))
print("op(2n) == [nu/(q^2;q^2)] mod 2:", all((int(S[2*i])-F[i])%2==0 for i in range(N)))
print("op(odd) even:", bool(np.all(S[1::2]%2==0)))
