import numpy as np, math
from collections import Counter
S1=np.load('op1_40000.npy'); S2=np.load('op2_40000.npy')
A2=S2[0::2]; Nm=len(A2)
D=np.zeros(8*Nm+2,dtype=np.int64)
for d in range(1,8*Nm+2,2): D[d::d]+= (1 if d%4==1 else -1)
Dm=np.array([D[8*m+1] for m in range(Nm)])
diff=(A2-Dm)%8
print("op2(2m)-D(8m+1) mod 8 values:", Counter(diff.tolist()))
odd=[m for m in range(Nm) if diff[m]==4]
print("first m with diff 4:", odd[:30])
print("8m+1:", [8*m+1 for m in odd[:20]])
def fac(n):
    f={};d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
print([fac(8*m+1) for m in odd[:20]])
