import numpy as np
N=20000
def ser(exps):
    c=np.zeros(N,dtype=np.int64)
    for e in exps:
        if 0<=e<N: c[e]^=1
    return c
K=range(-200,201)
P=ser([k*(3*k-1)//2 for k in K])            # f(Q,Q^2) = sum Q^{pent}
u=lambda s: ser([s*k*(3*k+2) for k in K])    # u(Q^s)
psi3=ser([3*n*(n+1)//2 for n in range(0,200)])
f8=ser([8*k*(3*k-1)//2 for k in K])
f3c=psi3  # psi(Q^3)
mul=lambda a,b: np.convolve(a,b)[:N]%2
lhs=mul(P,u(2)); t=mul(psi3,u(4)); lhs[1:]^=t[:N-1]
rhs=mul(psi3,f8)
print("P(Q)u(Q^2)+Q psi(Q^3)u(Q^4) ≡ psi(Q^3) f8 mod 2:", np.array_equal(lhs,rhs))
# compare with actual class-2 components from data definitions
psi=ser([n*(n+1)//2 for n in range(0,300)])
X2=ser([2*y*y for y in range(1,200)]); X4=ser([4*y*y for y in range(1,200)])
A=mul(psi,(X2+X4)%2)
B=np.zeros(N,dtype=np.int64); f1=ser([k*(3*k-1)//2 for k in K]); f6c=ser([6*n*(n+1)//2 for n in range(0,200)])
t=mul(mul(f1,f6c),f8); B[1:]=t[:N-1]
print("psi*(X(q^2)+X(q^4)) ≡ q f1 f6^3 f8 on residue 2 mod 3:", np.array_equal(A[2::3],B[2::3]))
