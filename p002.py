  from math import ceil
  from math import log
  
  fn = lambda x : int((phi**x-(1-phi)**x)/5**0.5) #this is the fib seq for x
  maxn = ceil(log(4*10**6*5**0.5)/log(phi)) #back calculate the closest n to 4 million and take the ceiling using fn
  sol = sum([i for i in [fn(i) for i in range(maxn)] if i%2==0]) #O(n), I sense there is a way to do this in O(1) using the integral of the fib sequence and replicating the solution of n
  
  print(sol)
