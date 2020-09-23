from math import factorial
def C(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

print( C(20,2))
