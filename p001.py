from math import ceil

sumn = lambda n : (n*(n-1)/2)
sumab = lambda a,b : sumn(ceil(a/b))*b

sol = sumab(1000,3)+sumab(1000,5) - sumab(1000,15) # O(1)

print(sol)
