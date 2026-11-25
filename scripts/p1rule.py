import math
def rep(p,a,b,c):
    for y in range(0,int(math.isqrt(4*a*p))+2):
        for x in range(-int(math.isqrt(p))-2,int(math.isqrt(p))+3):
            if a*x*x+b*x*y+c*y*y==p: return True
    return False
forms={'x2+32y2':(1,0,32),'x2+64y2':(1,0,64),'x2+72y2':(1,0,72),'x2+144y2':(1,0,144),'9x2+16y2':(9,0,16),'x2+24y2':(1,0,24),'x2+96y2':(1,0,96),'x2+48y2':(1,0,48),'x2+18y2':(1,0,18),'x2+36y2':(1,0,36),'x2+288y2':(1,0,288),'4x2+4xy+73y2':(4,4,73),'x2+576y2':(1,0,576)}
yes=[97,313,337]; no=[73,193,241]
def isprime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
more=[p for p in range(400,3000) if isprime(p) and p%24==1]
for p in yes+no:
    print(p, "FAMILY" if p in yes else "no", [k for k,f in forms.items() if rep(p,*f)])
