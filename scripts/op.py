import numpy as np, sys
def op1(N, M=1<<40):
    """coeffs of sum_{n>=0} (-q;q^2)_n^2 q^{2n}/(q^2;q^2)_n, mod M, up to q^{N-1}"""
    T=np.zeros(N,dtype=np.int64); T[0]=1; S=T.copy(); n=0
    while True:
        n+=1
        if 2*n>=N: break
        a=2*n-1
        for _ in range(2):           # *(1+q^a)
            T[a:]=(T[a:]+T[:-a])%M
        s=2*n                         # /(1-q^s)
        L=-(-N//s)*s; pad=np.zeros(L,dtype=np.int64); pad[:N]=T
        pad=pad.reshape(-1,s); pad=np.cumsum(pad,axis=0)%M; T=pad.reshape(-1)[:N].copy()
        T[2:]=T[:-2].copy(); T[:2]=0  # *q^2
        S=(S+T)%M
        if not T.any(): break
    return S
if __name__=="__main__":
    N=int(sys.argv[1]); S=op1(N); np.save('op1_%d.npy'%N,S); print(S[:30])
