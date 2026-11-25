import numpy as np
N=20000
def eta2(k):
    c=np.zeros(N,dtype=np.int64); j=0
    while True:
        a=k*j*(3*j-1)//2; b=k*j*(3*j+1)//2
        if a>=N: break
        c[a]^=1
        if j and b<N: c[b]^=1
        j+=1
    return c
def inv2(a):
    b=np.zeros(N,dtype=np.int64); b[0]=1
    for n in range(1,N):
        b[n]=int(np.dot(a[1:n+1],b[n-1::-1][:n]))%2
    return b
def mul(a,b): return np.convolve(a,b)[:N]%2
f={k:eta2(k) for k in (1,2,3,4,6,8,12)}
pw=lambda a,e: a if e==1 else mul(a,pw(a,e-1))
lhs=(mul(mul(f[1],pw(f[6],3)),inv2(f[2])) + np.roll(mul(mul(pw(f[3],3),pw(f[12],3)),inv2(f[4])),1))%2
rhs=mul(pw(f[3],3),f[8])
print("mod-2 identity f1 f6^3/f2 + q f3^3 f12^3/f4 = f3^3 f8 holds to q^%d:"%(N-1), np.array_equal(lhs[1:],rhs[1:]) and lhs[0]==rhs[0])
