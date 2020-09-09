#from eulerlib import numtheory #they're divisor system is too complex for this problem and slows it to a craw;
from math import ceil

def num_factors(x):
  n = 1
  for i in range( 2,ceil(x**0.5)):
    if x%i ==0:
      n+=1
  
  return n


i=5
fn = lambda n : n*(n+1)/2 
while num_factors(fn(i))<=500:
  i+=1
print(fn(i))
