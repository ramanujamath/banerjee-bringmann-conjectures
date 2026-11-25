import numpy as np, sys
M=1<<40
def mul1(c,a,s=1):   # c*(1+s q^a)
    c=c.copy(); c[a:]=(c[a:]+s*c[:-a])%M; return c
def div1(c,a,s=1):   # c/(1 + s q^a)   (s=-1 means 1/(1-q^a))
    N=len(c); L=-(-N//a)*a; p=np.zeros(L,dtype=np.int64); p[:N]=c; p=p.reshape(-1,a)
    if s==-1: p=np.cumsum(p,axis=0)%M
    else:
        sg=np.where(np.arange(p.shape[0])%2==0,1,-1)[:,None]
        p=(sg*(np.cumsum((sg*p)%M,axis=0)%M))%M
    return p.reshape(-1)[:N].copy()
def shift(c,s):
    d=np.zeros_like(c); d[s:]=c[:len(c)-s]; return d
def op2(N):
    # g2(-q;q^2) = sum_n (-q^2;q^2)_n q^{n(n+1)} / (-q;q^2)_{n+1}^2
    T=np.zeros(N,dtype=np.int64); T[0]=1
    T=div1(div1(T,1),1); G=T.copy(); n=0
    while True:
        n+=1
        if n*(n+1)>=N: break
        T=mul1(T,2*n); T=shift(T,2*n); T=div1(div1(T,2*n+1),2*n+1); G=(G+T)%M
    # prefactor (-q;q^2)^2 / (q^4;q^4)
    for j in range(1,N,2): G=mul1(mul1(G,j),j)
    for j in range(4,N,4): G=div1(G,j,-1)
    return G
if __name__=="__main__":
    N=int(sys.argv[1]); S=op2(N); np.save('op2_%d.npy'%N,S); print(S[:25].tolist())
