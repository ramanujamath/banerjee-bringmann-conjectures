import numpy as np, math
val=np.load('op1_4m_mod4.npy').astype(np.int64); N=200000; val=val[:N]
L=8*N+2
D=np.zeros(L,dtype=np.int64)
for d in range(1,L,2): D[d::2*d]+=(1 if d%4==1 else -1)
Dm=D[1::8][:N]
c=((val-Dm)%4)//2
# candidate: representation counts of n=8m+1 (or 3n+8=24m+11) by binary forms, halved mod 2
def reps(form,Nmax):
    a,b,cc=form; r=np.zeros(Nmax+1,dtype=np.int64)
    X=int(math.isqrt(4*Nmax))+2
    for x in range(-X,X+1):
        for y in range(-X,X+1):
            v=a*x*x+b*x*y+cc*y*y
            if 0<v<=Nmax: r[v]+=1
    return r
Nmax=8*20000+1
cands={}
for f in [(1,0,2),(1,0,8),(1,0,32),(1,0,16),(1,0,4),(2,0,3),(1,0,6),(3,0,8),(1,0,24),(1,0,48),(1,0,72),(1,0,18),(2,0,9),(1,0,3),(1,0,12),(3,0,16),(1,0,96),(1,0,144),(4,4,9),(1,0,36)]:
    r=reps(f,Nmax); cands[f]=r
m=np.arange(20000); n=8*m+1
for f,r in cands.items():
    for div in (1,2,4,8):
        x=(r[n]//div)%2
        if np.array_equal(x,c[:20000]): print("MATCH c ≡ r_%s(8m+1)/%d mod 2"%(str(f),div))
# also against 24m+11
n2=24*m[:6000]+11
for f in cands:
    r=reps(f,24*6000+12)
    for div in (1,2,4,8):
        if np.array_equal((r[n2]//div)%2,c[:6000]): print("MATCH c ≡ r_%s(24m+11)/%d"%(str(f),div))
print("done")
