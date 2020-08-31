from math import floor

def is_pal(x):
    s = str(x)
    k = len(s)
    y = True
    for i in range(floor(k/2)):
        c1 = s[i]
        c2 = s[k-i-1]
        if c1 != c2:
            y = False
    return y
    
i=1000**2-1

def FF(N):  #Ferrier Factorization of N
    a = ceil(N**0.5)
    b2 = a**2 - N
    while (int(b2**0.5)-b2**0.5) != 0:
        a+=1
        b2 = a**2-N

    return a-b2**0.5
while i>100**2:
    if is_pal(i):
        lhs = int(FF(i))
        rhs = int(i/lhs)
        if len(str(lhs))==3 and len(str(rhs))==3:
            print(i)
            i=0
    i-=1


