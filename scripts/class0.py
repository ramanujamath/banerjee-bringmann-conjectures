import numpy as np, math
val=np.load('op1_4m_mod4.npy').astype(np.int64)
M=300000; Nmax=8*M+2
def reps(a,c):
    r=np.zeros(Nmax+1,dtype=np.int64)
    X=math.isqrt(Nmax//a)+1; xs=np.arange(-X,X+1)
    for y in range(-math.isqrt(Nmax//c)-1, math.isqrt(Nmax//c)+2):
        v=a*xs*xs+c*y*y; v=v[(v>0)&(v<=Nmax)]; np.add.at(r,v,1)
    return r
R={k:reps(1,k) for k in (32,144,24,96,72,16,8)}; R['9,16']=reps(9,16); R['3,8']=reps(3,8)
m=np.arange(M); idx=m[m%3==0]; N=8*idx+1
s=R[144][N]+R['9,16'][N]+R[24][N]-R[96][N]+R[72][N]
print("all divisible by 4:", np.all(s%4==0))
sq=(np.array([math.isqrt(int(n))**2==int(n) for n in N])).astype(np.int64)
pred=(R[32][N]//2 + 2*((s//4+sq)%2))%4
print("class 0 formula holds for m<%d:"%M, bool(np.all(pred==val[idx])))
