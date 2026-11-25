def series(ex,N):
    c=[0]*N; c[0]=1
    for k,e in ex.items():
        for j in range(k,N,k):
            for _ in range(abs(e)):
                if e>0:
                    for i in range(N-1,j-1,-1): c[i]-=c[i-j]
                else:
                    for i in range(j,N): c[i]+=c[i-j]
    return c
def congr(c,m,Amax=60,minlen=25):
    found=[]
    for A in range(2,Amax+1):
        for B in range(A):
            if any(A%a==0 and B%a==b for a,b in found): continue
            v=c[B::A]
            if len(v)>=minlen and all(x%m==0 for x in v): found.append((A,B))
    return found
