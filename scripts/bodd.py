import numpy as np
from op2 import mul1, div1, shift, M
from modfit import search
N=12000
T=np.zeros(N,dtype=np.int64); T[0]=1; T=div1(div1(T,1,-1),1,-1); B=T.copy(); n=0
while True:
    n+=1
    if n*(n+1)>=N: break
    T=mul1(T,2*n); T=shift(T,2*n); T=div1(div1(T,2*n+1,-1),2*n+1,-1); B=(B+T)%M
np.save('B.npy',B)
beta=(B[1::2]//2)%2      # b(2n+1)/2 mod 2
for r in range(2):
    s=beta[r::2]
    print("beta(2n+%d) mod2 density:"%r, s.mean(), " eta fit:", search(list(s),2)[:2])
odd=[n for n in range(len(beta)) if beta[2*n+1 if False else n]]
print("first n with beta odd:", [n for n in range(200) if beta[n]][:40])
