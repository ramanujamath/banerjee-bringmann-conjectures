from fractions import Fraction as Fr
def sigma(n): return sum(d for d in range(1,n+1) if n%d==0)
def logder(T,N):
    # a_n with q T'/T = sum a_n q^n, T[0] must be nonzero
    t0=T[0]; T=[Fr(x,1)/t0 for x in T[:N]]
    # U = 1/T
    U=[Fr(0)]*N; U[0]=Fr(1)
    for n in range(1,N): U[n]=-sum(T[k]*U[n-k] for k in range(1,n+1))
    D=[n*T[n] for n in range(N)]
    return [sum(D[k]*U[n-k] for k in range(n+1)) for n in range(N)]
def fit(T,N=80,ks=(1,2,3,4,6,8,12,16,24,32,48)):
    """try T = c * q^s * prod f_k^{e_k}; returns (s,c,exps) or None"""
    s=next(i for i,x in enumerate(T) if x)
    T=T[s:]; c=T[0]; a=logder(T,N)
    # a_n = -sum_k e_k * k*sigma(n/k)
    import itertools
    rows=[[ -k*sigma(n//k) if n%k==0 else 0 for k in ks] for n in range(1,N)]
    rhs=[a[n] for n in range(1,N)]
    # gaussian elimination over rationals
    m=len(ks); A=[[Fr(x) for x in r]+[r2] for r,r2 in zip(rows,rhs)]
    piv=[];r=0
    for col in range(m):
        p=next((i for i in range(r,len(A)) if A[i][col]!=0),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]; pv=A[r][col]; A[r]=[x/pv for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][col]!=0:
                f=A[i][col]; A[i]=[x-f*y for x,y in zip(A[i],A[r])]
        piv.append(col); r+=1
    if any(all(x==0 for x in row[:-1]) and row[-1]!=0 for row in A): return None
    e={ks[col]:A[i][-1] for i,col in enumerate(piv)}
    if any(v.denominator!=1 for v in e.values()): return None
    return s,c,{k:int(v) for k,v in e.items() if v}
