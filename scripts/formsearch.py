import numpy as np, math, itertools
val=np.load('op1_4m_mod4.npy').astype(np.int64)
M=30000; Nmax=8*M+2
def reduced_forms(D):  # D<0
    out=[]
    a=1
    while 3*a*a<=-D:
        for b in range(-a+1,a+1):
            if (b*b-D)%(4*a)==0:
                c=(b*b-D)//(4*a)
                if c>=a and not (b<0 and (a==c)):
                    if math.gcd(math.gcd(a,abs(b)),c)>=1: out.append((a,b,c))
        a+=1
    return out
def reps(a,b,c):
    r=np.zeros(Nmax+1,dtype=np.int64); D=4*a*c-b*b
    Y=int(math.isqrt(4*a*Nmax//D))+2
    for y in range(-Y,Y+1):
        disc=b*b*y*y-4*a*(c*y*y-Nmax)
        if disc<0: continue
        s=math.isqrt(disc); lo=(-b*y-s)//(2*a)-1; hi=(-b*y+s)//(2*a)+1
        x=np.arange(lo,hi+1); v=a*x*x+b*x*y+c*y*y
        v=v[(v>0)&(v<=Nmax)]; np.add.at(r,v,1)
    return r
forms=[]
for D in (-128,-384,-1152,-512,-1536,-4608,-288,-96,-32):
    forms+= [f for f in reduced_forms(D)]
forms=sorted(set(forms))
print(len(forms),"forms")
R={f:reps(*f) for f in forms}
m=np.arange(M); N=8*m+1
for cls in (0,1):
    idx=m[m%3==cls][:4000]; t=val[idx]
    feats={f:R[f][N[idx]] for f in forms if R[f][N[idx]].any()}
    keys=list(feats)
    found=False
    for k in (1,2):
        for combo in itertools.combinations(keys,k):
            for coefs in itertools.product((1,-1,2),repeat=k):
                s=sum(c*feats[f] for c,f in zip(coefs,combo))
                for div in (2,4):
                    if np.all(s%div==0) and np.array_equal((s//div)%4,t):
                        print("class",cls,"val ≡ (",list(zip(coefs,combo)),")/%d mod 4"%div); found=True
    if not found: print("class",cls,": no 1-2 form combination found")
