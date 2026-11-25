import numpy as np
S=np.load('op2_40000.npy'); N=len(S)
primes=[p for p in range(3,140) if all(p%d for d in range(2,int(p**.5)+1))]
for p in primes:
    ok=all(np.all(S[2*p*p*0+(p*p-1)//4+2*p*k::2*p*p]%4==0) for k in range(1,p))
    cnt=len(S[(p*p-1)//4+2*p::2*p*p])
    print(p, p%8, "holds" if ok else "FAILS", "(#terms per progression ~%d)"%cnt)
print("odd-index mod 4 values:", np.unique(S[1::2]%4)[:5], " even-index:", np.unique(S[0::2]%4))
