import numpy as np, math
val=np.load('op1_4m_mod4.npy').astype(np.int64)
M=300000; Nmax=8*M+2
def reps(a,c):
    r=np.zeros(Nmax+1,dtype=np.int64)
    X=math.isqrt(Nmax//a)+1; xs=np.arange(-X,X+1)
    for y in range(-math.isqrt(Nmax//c)-1, math.isqrt(Nmax//c)+2):
        v=a*xs*xs+c*y*y; v=v[(v>0)&(v<=Nmax)]; np.add.at(r,v,1)
    return r
R={k:reps(1,k) for k in (32,8,16)}; R38=reps(3,8); R332=reps(3,32)
m=np.arange(M); idx=m[m%3==1]; N=8*idx+1
M9=np.where(N%9==0,N//9,0); N3=N//3
g=lambda arr,n: np.where(n>0,arr[n],0)
s=R[8][N]+g(R[16],M9)+R38[N3]-R332[N3]
sq=np.array([1 if x>0 and math.isqrt(int(x))**2==int(x) else 0 for x in M9])
print("class-1 sum divisible by 4:", bool(np.all(s%4==0)))
print("class-1 simplified formula, m<%d:"%M, bool(np.all((R[32][N]//2+2*((s//4+sq)%2))%4==val[idx])))
# odd-power families (exponent 3) for p ≡ 13,23 mod 24 and p≡17 non-rep
valall=val; Nall=8*np.arange(len(val))+1
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
tested=bad=0
for p in [q for q in range(5,120) if isprime(q)]:
    ok = p%24 in (13,23) or (p%24==17 and not any(math.isqrt(p-32*y*y)**2==p-32*y*y for y in range(1,int(math.isqrt(p//32))+1)))
    if not ok: continue
    for e in (1,3):
        mask=(Nall%(p**e)==0)&((Nall//p**e)%p!=0)
        tested+=int(mask.sum()); bad+=int(np.sum(valall[mask]!=0))
print("family check (exponents 1 and 3), cases:",tested,"failures:",bad)
