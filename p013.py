
f = open('p013.txt', 'r')
nums = f.read().split('\n')


print(sum([int(x) for x in nums]))
