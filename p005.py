#this one really isnt hard to code unless you make it modular so thats my prolbem
#the solutions pretty easy, just take the max prime factorization within the range given
#ie 2^4+3^2+5+7+11+13+17+19 = 232792560
from math import ceil

def FF(N): 
    div2 = False
    N2 = N==2
    while N%2 ==0:
        N/=2
        div2 = True
    if N==1 and div2 and not N2:
        return 2
    else:
        a = ceil(N**0.5)
        b2 = a**2 - N
        while (int(b2**0.5)-b2**0.5) != 0:
            a+=1
            b2 = a**2-N
    
        return a-b2**0.5
def min_ediv(R):
    mn = R[1]
    if R[0] == 0:
        mn = R[2]
    
    mx = R[-1]
    y = 1
    for i in range(mn,mx):
        isprime = FF(i)==1
        x=i
        if isprime:
            while x*i <=mx :
                x*=i
            y*=x
      
    return y
    
print(min_edev(range(1,21)) #1 to 20
