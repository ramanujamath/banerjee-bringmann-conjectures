from etafit import fit
N=400
def series_sum(terms):
    s=[0]*N
    for t in terms:
        for i in range(N): s[i]+=t[i]
    return s
def mulp(c,e,sign):  # c*(1+sign q^e)
    d=c[:]
    for i in range(e,N): d[i]+=sign*c[i-e]
    return d
def divp(c,e,sign):
    d=c[:]
    for i in range(e,N): d[i]-=sign*d[i-e]
    return d
def omega():
    tot=[0]*N; n=0
    while 2*n*(n+1)<N:
        t=[0]*N; t[2*n*(n+1)]=1
        for j in range(n+1):
            t=divp(divp(t,2*j+1,-1),2*j+1,-1)
        tot=[a+b for a,b in zip(tot,t)]; n+=1
    return tot
def Bfun():
    tot=[0]*N; n=0
    while n*(n+1)<N:
        t=[0]*N; t[n*(n+1)]=1
        for j in range(1,n+1): t=mulp(t,2*j,1)
        for j in range(n+1): t=divp(divp(t,2*j+1,-1),2*j+1,-1)
        tot=[a+b for a,b in zip(tot,t)]; n+=1
    return tot
for name,F in [("omega",omega()),("B",Bfun())]:
    for mod in (2,4):
        for r in range(mod):
            T=F[r::mod]
            print(name, f"coeffs {mod}n+{r}:", T[:8], "->", fit(T,N=len(T)-1 if len(T)<90 else 90))
