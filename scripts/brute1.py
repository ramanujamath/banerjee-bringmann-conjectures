import numpy as np
S=np.load('op1_40000.npy')
N=36
# op1^[1](n): even parts non-overlined (any multiplicity), largest part even, odd parts: weight 1 + 2x^j + x^{2j}
def evenparts(n,maxp):  # partitions into even parts <= maxp
    if n==0: return 1
    return sum(evenparts(n-p,p) for p in range(min(n,maxp),1,-1) if p%2==0)
def odd_ways(n,bound):
    c=[0]*(n+1); c[0]=1
    for j in range(1,min(bound,n+1),2):
        d=c[:]
        for i in range(n+1):
            if i>=j: d[i]+=2*c[i-j]
            if i>=2*j: d[i]+=c[i-2*j]
        c=d
    return c
out=[1]
for n in range(1,N):
    tot=0
    for L in range(2,n+1,2):          # largest part L (even), at least one L
        for a in range(L,n+1):         # even-part total a, containing L as largest
            e=evenparts(a-L,L)
            if e: tot+=e*odd_ways(n-a,L)[n-a]
    out.append(tot)
print(out); print("matches:", out==[int(x) for x in S[:N]])
