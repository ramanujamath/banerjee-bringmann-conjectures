import numpy as np
from op2 import mul1, div1, M
W=np.load('omega.npy'); N=len(W)
def eta(ex,N):
    c=np.zeros(N,dtype=np.int64); c[0]=1
    for k,e in ex.items():
        for j in range(k,N,k):
            for _ in range(abs(e)): c = mul1(c,j,-1) if e>0 else div1(c,j,-1)
    return c
def sub(c,k):  # c(q^k)
    d=np.zeros(N,dtype=np.int64); d[::k]=c[:-(-N//k)][:len(d[::k])]; return d
def mul(a,b): 
    r=np.zeros(N,dtype=object); A=[int(x) for x in a]; B=[int(x) for x in b]
    out=[0]*N
    for i,x in enumerate(A):
        if x:
            for j in range(N-i):
                if B[j]: out[i+j]+=x*B[j]
    return np.array([o%M for o in out],dtype=np.int64)
# f(q) third order: sum q^{n^2}/(-q;q)_n^2
f=np.zeros(N,dtype=np.int64); n=0
while n*n<N:
    t=np.zeros(N,dtype=np.int64); t[n*n]=1
    for j in range(1,n+1): t=div1(div1(t,j),j)
    f=(f+t)%M; n+=1
Wm=W.copy(); Wm[1::2]=(-Wm[1::2])%M   # omega(-q)
lhs=(sub(f,8)+2*np.roll(W,1)+2*np.roll(sub(Wm,4),3))%M; lhs[0]=sub(f,8)[0]
phi=eta({2:5,1:-2,4:-2},N); G=mul(mul(phi,sub(phi,2)),sub(phi,2)); G=mul(G,eta({4:-2},N))
L=N//2
print("Watson/APSY identity:", np.array_equal(lhs[:L],G[:L]))
print("f(q)*f1 ≡ 1 mod 4:", bool(np.all(mul(f,eta({1:1},N))[1:L]%4==0)))
oct_=set(2*j*(3*j-2) for j in range(-200,200))
print("omega(m) odd iff m=2j(3j-2):", all((W[m]%2==1)==(m in oct_) for m in range(N)))
