import numpy as np, math
from collections import Counter, defaultdict
val=np.load('op1_4m_mod4.npy').astype(np.int64)
def isprime(n):
    if n<2: return False
    for d in range(2,int(n**.5)+1):
        if n%d==0: return False
    return True
def repd(n,k):  # is n = x^2 + k y^2 with y != 0
    for y in range(1,int(math.isqrt(n//k))+1):
        x2=n-k*y*y; x=math.isqrt(x2)
        if x*x==x2: return True
    return False
stats=defaultdict(Counter)
for m in range(1,60000):
    N=8*m+1
    if isprime(N):
        key=(N%8, N%3, repd(N,16) if N%8==1 else None, repd(N,64) if N%8==1 else None, repd(N,48) if N%3==1 else None)
        stats[key][int(val[m])]+=1
for k in sorted(stats, key=str): print(k, dict(stats[k]))
