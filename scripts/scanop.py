import numpy as np
S1=np.load('op1_40000.npy'); S2=np.load('op2_40000.npy')
def scan(S,m,Amax=300,minlen=60):
    found=[]
    for A in range(2,Amax+1):
        for B in range(A):
            if any(A%a==0 and B%a==b for a,b in found): continue
            v=S[B::A]
            if len(v)>=minlen and np.all(v%m==0): found.append((A,B))
    return found
for name,S in [("op1",S1),("op2",S2)]:
    for m in [3,4,5,7,8,16]:
        r=scan(S,m)
        print(name,"mod",m,":",len(r),r[:30],flush=True)
