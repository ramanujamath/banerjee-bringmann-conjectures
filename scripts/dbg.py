import numpy as np
N=3000
def theta_psi(k):
    c=np.zeros(N,dtype=np.int64); n=0
    while k*n*(n+1)//2<N: c[k*n*(n+1)//2]+=1; n+=1
    return c
def eta2(k):  # f_k mod 2 via pentagonal
    c=np.zeros(N,dtype=np.int64); j=0
    while True:
        a=k*j*(3*j-1)//2; b=k*j*(3*j+1)//2
        if a>=N: break
        c[a]^=1
        if j and b<N: c[b]^=1
        j+=1
    return c
def mul(a,b): return np.convolve(a,b)[:N]%2
psi=theta_psi(1); psi16=theta_psi(16)
A=np.zeros(N,dtype=np.int64); A[2:]=mul(psi,psi16)[:N-2]
B=np.zeros(N,dtype=np.int64); t=mul(mul(eta2(1),mul(eta2(6),mul(eta2(6),eta2(6)))),eta2(8)); B[1:]=t[:N-1]
print("A≡B on exponents ≡2 mod 3:", np.array_equal(A[2::3],B[2::3]))
print("A_2 first:", np.nonzero(A[2::3])[0][:15]); print("B_2 first:", np.nonzero(B[2::3])[0][:15])
f1f8=mul(eta2(1),eta2(8)); print("f1f8 mod2 first exps:", np.nonzero(f1f8)[0][:12])
