def collatz(x):
    
    n = x
    l = [n]
    while n >1:
        if n%2==0:
            n/=2
        else:
            n = n*3+1
        l.append(n)
    return l


n = 10**6
maxl = []
while n>1:
    l = collatz(n)
    n-=1
    if len(l)>len(maxl):
        maxl = l
print(maxl)
