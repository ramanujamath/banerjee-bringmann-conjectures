import numpy as np, itertools, sys
L=300
def f(k,L):
    c=np.zeros(L,dtype=np.int64); c[0]=1
    for j in range(k,L,k):
        c[j:]=c[j:]-c[:-j].copy() if False else c[j:]
        d=c.copy(); d[j:]-=c[:-j]; c=d
    return c
def inv(a,mod):
    b=np.zeros(len(a),dtype=np.int64); b[0]=1
    for n in range(1,len(a)): b[n]=(-np.dot(a[1:n+1],b[n-1::-1][:n]))%mod
    return b
def conv(a,b,mod): return np.convolve(a,b)[:len(a)]%mod
def powers(mod,ks,E):
    P={}
    for k in ks:
        base=f(k,L)%mod; ib=inv(base,mod)
        P[(k,0)]=np.eye(1,L,0,dtype=np.int64)[0]
        for e in range(1,E+1):
            P[(k,e)]=conv(P[(k,e-1)],base,mod); P[(k,-e)]=conv(P[(k,-e+1)],ib,mod)
    return P
def search(T,mod,ks=(1,2,4,8,16),E=3,consts=None):
    T=np.array(T[:L],dtype=np.int64)%mod
    s=int(np.argmax(T!=0)); T=np.roll(T,-s); T[L-s:]=0; Lc=L-s-1
    P=powers(mod,ks,E); hits=[]
    consts=consts or [c for c in range(1,mod) if np.gcd(c,mod)==1]
    for es in itertools.product(range(-E,E+1),repeat=len(ks)):
        c=P[(ks[0],es[0])]
        for k,e in zip(ks[1:],es[1:]):
            if e: c=conv(c,P[(k,e)],mod)
        for cc in consts:
            if np.array_equal((cc*c[:Lc])%mod,T[:Lc]): hits.append((s,cc,{k:e for k,e in zip(ks,es) if e}))
    return hits
if __name__=="__main__":
    S1=np.load('op1_40000.npy'); S2=np.load('op2_40000.npy')
    jobs=[("op1(4m) mod4",S1[0::4],4),("op1(4m+2) mod4",S1[2::4],4),("op1(2m+1)/2 mod2",S1[1::2]//2,2),
          ("op1(2m+1) mod4",S1[1::2],4),("op2(2m+1) mod4",S2[1::2],4),("op2(4m+1) mod 4",S2[1::4],4),("op2(4m+3) mod4",S2[3::4],4)]
    for name,T,mod in jobs:
        h=search(list(T),mod); print(name, h[:4], len(h), flush=True)
