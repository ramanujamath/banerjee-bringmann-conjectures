import numpy as np
from etafit import fit
S1=np.load('op1_40000.npy'); S2=np.load('op2_40000.npy')
for name,S in [("op1",S1),("op2",S2)]:
    for mod in (2,4,8):
        for r in range(mod):
            T=[int(x) for x in S[r::mod][:120]]
            if not any(T): print(name,f"{mod}n+{r}: all zero"); continue
            print(name, f"{mod}n+{r}:", T[:6], "->", fit(T,N=100), flush=True)
