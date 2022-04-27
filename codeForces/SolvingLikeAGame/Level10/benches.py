import math

n = int(input())

m  = int(input())

maxim = 0

arr = [] 

for _ in range(n):
    el = int(input())

    maxim = max(maxim, el)

    arr.append(el)

maxRes = maxim+m

avail = 0

for i in arr: avail+= (maxim- i)

m-= avail

if m < 0:
    rem = 0
else:
    rem = math.ceil(m/n)

minRes = maxim+ rem

print(minRes, maxRes)