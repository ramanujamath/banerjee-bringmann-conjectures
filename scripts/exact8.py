import numpy as np
from op2 import mul1, div1, M
S2=np.load('op2_40000.npy'); A=S2[0::2]; B=np.load('B.npy'); N=min(len(A),len(B)//2)
def eta(ex,N):
    c=np.zeros(N,dtype=np.int64); c[0]=1
    for k,e in ex.items():
        for j in range(k,N,k):
            for _ in range(abs(e)): c = mul1(c,j,-1) if e>0 else div1(c,j,-1)
    return c
H=eta({2:2,4:5,1:-5,8:-2},N)
K=eta({8:2,1:-1,2:-1,4:-1},N)
bo=B[1::2][:N]
# K * bo  (mod M) via numpy convolution in chunks with python ints mod M
prod=np.zeros(N,dtype=object)
Ko=[int(x) for x in K]; Bo=[int(x) for x in bo]
pr=[0]*N
for i in range(N):
    if Ko[i]:
        ki=Ko[i]
        for j in range(N-i): pr[i+j]+=ki*Bo[j]
T=[0]*N
for i in range(N-1): T[i+1]=(2*pr[i])%M
ok=all((int(A[m])-int(H[m])+T[m])%M==0 for m in range(N))
print("exact identity for op2(2m), m <",N,":",ok)
