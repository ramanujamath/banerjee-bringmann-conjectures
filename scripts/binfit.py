import numpy as np, math, itertools
val=np.load('op1_4m_mod4.npy').astype(np.int64)
M=60000; Nmax=8*M+1
def reps(a,b,c):
    r=np.zeros(Nmax+1,dtype=np.int64)
    # enumerate x,y with a x^2+bxy+c y^2 <= Nmax (positive definite)
    D=4*a*c-b*b
    Y=int(math.isqrt(4*a*Nmax//D))+2
    for y in range(-Y,Y+1):
        # solve a x^2 + b y x + c y^2 <= Nmax
        disc=b*b*y*y-4*a*(c*y*y-Nmax)
        if disc<0: continue
        s=math.isqrt(disc); lo=(-b*y-s)//(2*a)-1; hi=(-b*y+s)//(2*a)+1
        x=np.arange(lo,hi+1); v=a*x*x+b*x*y+c*y*y
        v=v[(v>0)&(v<=Nmax)]; np.add.at(r,v,1)
    return r
forms=[(1,0,32),(4,4,9),(3,2,11),(1,0,16),(1,0,8),(1,0,2),(1,0,64),(4,0,9),(1,0,72),(1,0,18),(2,0,9),(1,0,36),(4,4,19),(5,2,13),(1,0,128),(1,0,48),(3,0,16),(1,0,24),(1,0,96),(1,0,288),(9,0,32),(4,4,73),(1,0,144),(8,0,9),(1,0,6),(2,0,3),(1,0,3),(1,0,12),(3,0,4)]
R={f:reps(*f) for f in forms}
m=np.arange(M); N=8*m+1
L=8*M+2
Dsum=np.zeros(L,dtype=np.int64)
for d in range(1,L,2): Dsum[d::2*d]+=(1 if d%4==1 else -1)
DN=Dsum[N]
for cls in range(3):
    idx=m[m%3==cls]
    target=val[idx]
    for f in forms:
        for k in (1,2,4,8):
            if np.array_equal((R[f][N[idx]]//k)%4,target): print("class",cls,": val ≡ r_%s(N)/%d mod 4"%(str(f),k))
            if np.array_equal((DN[idx]+2*((R[f][N[idx]]//k)%2))%4,target): print("class",cls,": val ≡ D(N)+2*(r_%s(N)/%d) mod 4"%(str(f),k))
    for f,g in itertools.combinations(forms,2):
        for k in (2,4):
            if np.array_equal(((R[f][N[idx]]-R[g][N[idx]])//k)%4,target): print("class",cls,": val ≡ (r_%s - r_%s)/%d"%(f,g,k))
            if np.array_equal(((R[f][N[idx]]+R[g][N[idx]])//k)%4,target): print("class",cls,": val ≡ (r_%s + r_%s)/%d"%(f,g,k))
print("done")
