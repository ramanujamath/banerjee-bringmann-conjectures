import numpy as np
N=20000
def psi(k):
    c=np.zeros(N,dtype=object); n=0
    while k*n*(n+1)//2<N: c[k*n*(n+1)//2]+=1; n+=1
    return c
def phi(k):
    c=np.zeros(N,dtype=object); c[0]=1; n=1
    while k*n*n<N: c[k*n*n]+=2; n+=1
    return c
def mul(a,b):
    out=np.zeros(N,dtype=object); nz=np.nonzero(a)[0]
    for i in nz: out[i:]+=a[i]*b[:N-i]
    return out
lhs=mul(psi(1),psi(3))
r2=mul(phi(2),psi(12)); rhs=mul(phi(6),psi(4)); rhs[1:]+=r2[:N-1]
print("psi(q)psi(q^3) = phi(q^6)psi(q^4) + q phi(q^2)psi(q^12) exactly to q^%d:"%(N-1), all(lhs==rhs))
# mod-2 chain checks
def eta2(k):
    c=np.zeros(N,dtype=np.int64); j=0
    while True:
        a=k*j*(3*j-1)//2; b=k*j*(3*j+1)//2
        if a>=N: break
        c[a]^=1
        if j and b<N: c[b]^=1
        j+=1
    return c
m2=lambda a,b: np.convolve(a,b)[:N]%2
def pw(a,e):
    r=np.zeros(N,dtype=np.int64); r[0]=1
    for _ in range(e): r=m2(r,a)
    return r
f1,f3=eta2(1),eta2(3)
lhs2=(pw(f1,12)+m2(pw(f1,3),pw(f3,3)))%2
rhs2=np.zeros(N,dtype=np.int64); rhs2[1:]=pw(f3,12)[:N-1]
print("f1^12 + f1^3 f3^3 ≡ q f3^12 (mod 2):", np.array_equal(lhs2,rhs2))
