#This one sucks. There is no good solution

def seive_of_E(n):


  A = [1]*n
  maxn = int(n**0.5)
  for i in range(2,maxn):
      if A[i] == 1:
          p = 0
          j = i**2+p*i
          while j<n:

              A[j] = 0
              p+=1
              j = i**2+p*i

  return A
  
i=1
while sum(seive_of_E(i))<10001:
    i+=1
print(i-1)
    
    
    
