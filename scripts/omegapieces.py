import numpy as np
from modfit import search
from op2 import div1, M
N=6000
T=np.zeros(N,dtype=np.int64); W=np.zeros(N,dtype=np.int64); n=0
while 2*n*(n+1)<N:
    t=np.zeros(N,dtype=np.int64); t[2*n*(n+1)]=1
    for j in range(n+1): t=div1(div1(t,2*j+1,-1),2*j+1,-1)
    W=(W+t)%M; n+=1
np.save('omega.npy',W)
for r in range(4):
    h=search(list(W[r::4]),2); print("omega 4n+%d mod 2:"%r, h[:3], flush=True)
print("omega 4n+2 mod 2 nonzero count:", int(np.sum(W[2::4]%2)), " 4n+3:", int(np.sum(W[3::4]%2)))
