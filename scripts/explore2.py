import numpy as np, math
S=np.load('op2_40000.npy'); a=S[0::2]%4; M=len(a)
odd=[m for m in range(M) if a[m]%2]
print("a(m) odd at m:", odd[:25])
print("8m+1 for those:", [8*m+1 for m in odd[:15]])
print("all squares?", all(math.isqrt(8*m+1)**2==8*m+1 for m in odd), " squares count:", sum(1 for m in range(M) if math.isqrt(8*m+1)**2==8*m+1), len(odd))
# among even a(m): when ≡2 mod 4?
def factor(n):
    f={};d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
two=[m for m in range(200) if a[m]==2]
print("a(m)==2 at m:", two[:30])
print([ (8*m+1, factor(8*m+1)) for m in two[:14]])
