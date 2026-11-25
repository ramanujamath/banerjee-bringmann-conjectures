import numpy as np
from op2 import mul1, div1, shift, M
S=np.load('op2_40000.npy'); A=S[0::2]; Nm=len(A)
# (b) op(2m) ≡ sum_{d|8m+1} chi_{-4}(d) mod 4, via sieve
D=np.zeros(8*Nm+2,dtype=np.int64)
for d in range(1,8*Nm+2,2):
    D[d::d] += (1 if d%4==1 else -1)
pred=np.array([D[8*m+1] for m in range(Nm)])
print("op(2m) ≡ Σ χ_{-4}(d) (mod 4) for m <",Nm,":", bool(np.all((A-pred)%4==0)))
# (a) sum op(2m) q^m ≡ f4/f1 mod 4
N=Nm; c=np.zeros(N,dtype=np.int64); c[0]=1
for j in range(4,N,4): c=mul1(c,j,-1)
for j in range(1,N): c=div1(c,j,-1)
print("Σ op(2m) q^m ≡ f4/f1 (mod 4):", bool(np.all((A-c)%4==0)))
# (c) B(q) = Σ q^{n(n+1)} (-q^2;q^2)_n/(q;q^2)_{n+1}^2 : even part = f4^5/f2^4, odd coeffs even
N=8000; T=np.zeros(N,dtype=np.int64); T[0]=1; T=div1(div1(T,1,-1),1,-1); B=T.copy(); n=0
while True:
    n+=1
    if n*(n+1)>=N: break
    T=mul1(T,2*n); T=shift(T,2*n); T=div1(div1(T,2*n+1,-1),2*n+1,-1); B=(B+T)%M
e=np.zeros(N,dtype=np.int64); e[0]=1
for j in range(4,N,4):
    for _ in range(5): e=mul1(e,j,-1)
for j in range(2,N,2):
    for _ in range(4): e=div1(e,j,-1)
print("even part of B = f4^5/f2^4:", bool(np.all((B[0::2]-e[0::2])%M==0)) and bool(np.all(e[1::2]==0)))
print("odd coefficients of B even:", bool(np.all(B[1::2]%2==0)))
