import math

def nearestTwoPow(x):
    res = 0

    while x!= 1:
        res+=1
        x = x//2
    
    return int(math.pow(2, res))

n = int(input())

arr = list(map(int, input().split()))

prev = 0

for i in range(n-1):

    res = prev+ arr[i]
    print(res)

    prev = res

    distFromLast = n-i-1

    nearestDump = i+ nearestTwoPow(distFromLast)

    arr[nearestDump]+= arr[i]