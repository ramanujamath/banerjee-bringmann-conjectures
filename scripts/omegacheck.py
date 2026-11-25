import numpy as np, math
from op2 import mul1, div1, M
W=np.load('omega.npy'); N=len(W)//4
def eta(ex,N):
    c=np.zeros(N,dtype=np.int64); c[0]=1
    for k,e in ex.items():
        for j in range(k,N,k):
            for _ in range(abs(e)):
                c = mul1(c,j,-1) if e>0 else div1(c,j,-1)
    return c
print("ω(4n)   = f2^9/(f1^6 f4^2) exact:", np.array_equal(W[0::4][:N]%M, eta({1:-6,2:9,4:-2},N)))
print("ω(4n+1) = 2 f2^3 f4^2/f1^4 exact:", np.array_equal(W[1::4][:N]%M, (2*eta({1:-4,2:3,4:2},N))%M))
print("ω(4n+3) even:", bool(np.all(W[3::4]%2==0)))
odd=[n for n in range(len(W[2::4])) if W[4*n+2]%2]
print("n with ω(4n+2) odd:", odd[:20])
print("3n+? / 24n+?:", [(24*n+ 17) for n in odd[:12]], [math.isqrt(3*n+2) for n in odd[:5]])
