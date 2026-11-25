import numpy as np
from op2 import mul1, div1, M
S1=np.load('op1_40000.npy'); S2=np.load('op2_40000.npy')
A=S1[0::4]; N=len(A)
def eta(ex,N):
    c=np.zeros(N,dtype=np.int64); c[0]=1
    for k,e in ex.items():
        for j in range(k,N,k):
            for _ in range(abs(e)):
                c = mul1(c,j,-1) if e>0 else div1(c,j,-1)
    return c
t=eta({1:1,6:3,8:1},N); corr=np.zeros(N,dtype=np.int64); corr[1:]=t[:-1]
print("op1(4m) ≡ op2(2m) + 2[q^m] q f1 f6^3 f8 (mod 4):", bool(np.all((A - S2[0::2][:N] - 2*corr)%4==0)))
print("op1(4n+1) ≡ 0 mod 4 up to n<10000:", bool(np.all(S1[1::4]%4==0)))
