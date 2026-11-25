import itertools, sys
N=2000
def series(ex):  # ex: dict k->exponent, prod (1-q^k)^e
    c=[0]*N; c[0]=1
    for k,e in ex.items():
        if e>0:
            for _ in range(e):
                for i in range(N-1,k-1,-1): c[i]-=c[i-k]
        elif e<0:
            for _ in range(-e):
                for i in range(k,N): c[i]+=c[i-k]
    return c
primes=[3,5,7,11,13]
def find(c):
    res=[]
    for m in primes:
        for A in range(2,60):
            for B in range(A):
                vals=c[B::A]
                if len(vals)<20: continue
                if all(v%m==0 for v in vals):
                    # skip if implied by smaller A dividing
                    if any(A%a==0 and a<A and (B%a,m) in [(r[1],r[2]) for r in res if r[0]==a] for a in range(2,A)): continue
                    res.append((A,B,m))
    return res
ks=[1,2,3,4,6]
out=[]
for es in itertools.product([-2,-1,0,1,2],repeat=len(ks)):
    ex={k:e for k,e in zip(ks,es) if e}
    if not ex: continue
    c=series(ex)
    if all(v>=0 for v in c[:200]) and sum(1 for v in c[:200] if v)>150:
        r=find(c)
        if r: out.append((ex,r))
for ex,r in out: print(ex, r)
print(len(out))
