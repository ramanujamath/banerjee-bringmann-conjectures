import numpy as np
from op2 import div1, M
B=np.load('B.npy'); s=((B[3::4]//2)%2)[:2500]; L=len(s)
P=np.zeros(60000,dtype=np.int64); P[0]=1
for j in range(1,60000): P=div1(P,j,-1) if False else P
# partition numbers mod 2 quickly via pentagonal recurrence
N=60000; p=np.zeros(N,dtype=np.int64); p[0]=1
pent=[]
k=1
while True:
    a=k*(3*k-1)//2; b=k*(3*k+1)//2
    if a>=N: break
    pent.append((a,k)); 
    if b<N: pent.append((b,k))
    k+=1
for n in range(1,N):
    t=0
    for g,k in pent:
        if g>n: break
        t+= p[n-g]
    p[n]=t%2
hits=[]
for a in range(1,25):
    for b in range(a):
        seq=p[b::a][:L]
        if len(seq)==L:
            for sh in range(0,6):
                if np.array_equal(s[sh:],seq[:L-sh]) : hits.append((a,b,sh))
print("matches with p(an+b) mod 2 (shifted):", hits[:10])
