from math import ceil

#Fermat's factorization 
def FF(N): 
    while N%2 ==0:
        N/=2
    a = ceil(N**0.5)
    b2 = a**2 - N
    while int(b2**0.5)-b2**0.5 != 0:
        a+=1
        b2 = a**2-N

    return a-b2**0.5
    
    #prime factorization sucks.
def pfact(x):
    if x%2==0:
        x/=2
    lhs = FF(x)
    rhs = x/lhs
    if lhs ==1:
        return rhs
    else:
        lprime = pfact(lhs)
        rprime = pfact(rhs)
        return max([lprime, rprime])
        
print(pfact(600851475143))
