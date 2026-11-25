import numpy as np, itertools
S=np.load('op2_40000.npy'); A=S[0::2][:3000]%4; N=len(A)
def eta(ex,N,mod):
    c=np.zeros(N,dtype=np.int64); c[0]=1
    for k,e in ex.items():
        for j in range(k,N,k):
            for _ in range(abs(e)):
                if e>0: c[j:]=(c[j:]-c[:-j])%mod
                else:
                    L=-(-N//j)*j; p=np.zeros(L,dtype=np.int64); p[:N]=c
                    c=(np.cumsum(p.reshape(-1,j),axis=0)%mod).reshape(-1)[:N]
    return c%mod
psi=eta({2:2,1:-1},N,4)
X=((A-psi)%4)
print("A-psi all even:", np.all(X%2==0))
X=(X//2)%2
print("X first terms:", X[:40].tolist())
hits=[]
ks=[1,2,4,8,16]
for es in itertools.product(range(-3,4),repeat=5):
    ex={k:e for k,e in zip(ks,es) if e}
    for s in range(0,8):  # q^s shift
        c=eta(ex,N-s,2) if ex else None
        if c is None: continue
        if np.array_equal(X[s:s+400], c[:400]) and not X[:s].any():
            if np.array_equal(X[s:], c[:N-s]): hits.append((s,ex)); print("HIT", s, ex, flush=True)
    if len(hits)>5: break
