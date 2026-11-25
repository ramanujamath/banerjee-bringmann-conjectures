import numpy as np, time
N=1_000_000
t=time.time()
# D(8m+1) mod 4 via sieve of chi_{-4} divisor sum over odd numbers up to 8N+1
L=8*N+2
D=np.zeros(L,dtype=np.int32)
for d in range(1,L,2):
    D[d::2*d]+= (1 if d%4==1 else -1)   # multiples d*odd only (we only need odd n)
Dm=D[1::8][:N]%4      # n=8m+1
print("sieve",time.time()-t)
# c: coefficients of f1*f6^3*f8 mod 2 using sparse theta forms
def pent(scale,N):
    s=[];k=0
    while True:
        a=scale*k*(3*k-1)//2; b=scale*k*(3*k+1)//2
        if a>=N and b>=N: break
        if a<N: s.append(a)
        if k>0 and b<N: s.append(b)
        k+=1
    return sorted(set(s))
f1=np.zeros(N,dtype=np.uint8); f1[pent(1,N)]=1
f8=pent(8,N)
g=np.zeros(N,dtype=np.uint8)
for e in f8: g[e:]^=f1[:N-e]
tri6=[]; j=0
while 3*j*(j+1)<N: tri6.append(3*j*(j+1)); j+=1
h=np.zeros(N,dtype=np.uint8)
for e in tri6: h[e:]^=g[:N-e]
c=np.zeros(N,dtype=np.uint8); c[1:]=h[:N-1]   # q*f1 f6^3 f8
val=(Dm+2*c)%4
print("built",time.time()-t)
S1=np.load('op1_40000.npy'); chk=S1[0::4][:10000]%4
print("agrees with direct data m<10000:", bool(np.all(chk==val[:10000])))
np.save('op1_4m_mod4.npy',val.astype(np.int8))
# scan progressions m ≡ B mod A, A<=2000, primitive
found=[]
zero=(val==0)
for A in range(2,2001):
    for B in range(A):
        if any(A%a==0 and B%a==b for a,b in found): continue
        if zero[B::A].all(): found.append((A,B))
print("time",time.time()-t, "count",len(found))
print(found[:80])
np.save('found.npy',np.array(found))
