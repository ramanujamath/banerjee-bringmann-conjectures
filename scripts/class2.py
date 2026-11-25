import numpy as np, math
val=np.load('op1_4m_mod4.npy').astype(np.int64); M=len(val); Nmax=8*M+1
r=np.zeros(Nmax+1,dtype=np.int64)
X=math.isqrt(Nmax)
xs=np.arange(-X,X+1)
for y in range(-int(math.isqrt(Nmax//32))-1, int(math.isqrt(Nmax//32))+2):
    v=xs*xs+32*y*y; v=v[v<=Nmax]; np.add.at(r,v,1)
m=np.arange(M); idx=m[m%3==2]; N=8*idx+1
print("class 2 formula holds for all m<10^6:", bool(np.all((r[N]//2)%4==val[idx])))
# predicted families: m≡2 mod 3, prime q ≡5,7 mod 8 or (q≡1 mod 8 and q not x^2+32y^2) with q || 8m+1 -> 0 mod 4
def isprime(n):
    return n>1 and all(n%d for d in range(2,int(n**.5)+1))
bad=0; tested=0
for q in [p for p in range(3,400) if isprime(p)]:
    cls = q%8
    rep = r[q]>0
    if cls in (5,7) or (cls==1 and not rep):
        for mm in idx:
            Nn=8*mm+1
            if Nn%q==0 and (Nn//q)%q!=0:
                tested+=1
                if val[mm]!=0: bad+=1
print("predicted-zero cases tested:",tested," failures:",bad)
# q ≡ 3 mod 8 and q ≡1 mod 8 represented: how often zero
for q in [11,19,41,73,113]:
    vs=[val[mm] for mm in idx if (8*mm+1)%q==0 and ((8*mm+1)//q)%q!=0]
    print(q, q%8, "frac zero", np.mean(np.array(vs)==0), len(vs))
