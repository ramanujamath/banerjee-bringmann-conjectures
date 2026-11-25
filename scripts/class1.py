import numpy as np, math
val=np.load('op1_4m_mod4.npy').astype(np.int64)
L=20000
def ser(exps):
    c=np.zeros(L,dtype=np.int64)
    for e in exps:
        if 0<=e<L: c[e]^=1
    return c
K=range(-300,301)
P=lambda s=1: ser([s*k*(3*k-1)//2 for k in K])
psi=lambda s: ser([s*n*(n+1)//2 for n in range(0,400)])
u=lambda s: ser([s*k*(3*k+2) for k in K])
X=lambda s: ser([s*y*y for y in range(1,400)])
mul=lambda a,b: np.convolve(a,b)[:L]%2
sh=lambda a,k: np.concatenate([np.zeros(k,dtype=np.int64),a[:L-k]])
E1=(sh(mul(P(),u(4)),1) + mul(psi(3),(X(6)+X(12))%2) + mul(mul(P(),P(2)),psi(2)) + sh(mul(psi(3),mul(psi(6),psi(2))),1))%2
# r32 at N=24E+9
Nmax=24*L+10
def reps(a,c):
    r=np.zeros(Nmax+1,dtype=np.int64)
    Xm=math.isqrt(Nmax//a)+1; xs=np.arange(-Xm,Xm+1)
    for y in range(-math.isqrt(Nmax//c)-1, math.isqrt(Nmax//c)+2):
        v=a*xs*xs+c*y*y; v=v[(v>0)&(v<=Nmax)]; np.add.at(r,v,1)
    return r
R={(a,c):reps(a,c) for (a,c) in [(1,32),(1,16),(1,8),(3,8),(3,32)]}
E=np.arange(L); N=24*E+9
actual=val[1:3*L:3][:L]
print("direct theta class1:", np.array_equal((R[(1,32)][N]//2+2*E1)%4, actual))
def r(f,n): return R[f][n] if n>0 else 0
def sq(n): return 1 if n>0 and math.isqrt(n)**2==n else 0
pred=[]
for Ei in range(L):
    n=24*Ei+9; M9=n//9 if n%9==0 else 0
    U1=(r((1,32),n)-r((1,32),M9))//4
    U23=((r((1,16),M9)-2*sq(M9)) + (r((1,32),M9)-2*sq(M9)))//4 if M9 else 0
    U4=((r((1,8),n)-r((1,32),n)) - (r((1,8),M9)-r((1,32),M9)))//4
    U5=(r((3,8),n//3)-r((3,32),n//3))//4
    U6=(r((1,8),M9)-r((1,32),M9))//4 if M9 else 0
    pred.append((r((1,32),n)//2 + 2*((U1+U23+U4+U5+U6)%2))%4)
print("r-count class1 formula:", np.array_equal(np.array(pred),actual))
