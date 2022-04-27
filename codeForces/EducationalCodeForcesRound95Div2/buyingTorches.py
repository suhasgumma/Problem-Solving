import math
T = int(input())

for _ in range(T):
    x, y, k = map(int, input().split())

    totalSticks = k + (k*y)

    opsForSticks = (totalSticks-2)//(x-1)

    opsForCoal = k

    totalMinOps = math.ceil(opsForCoal+opsForSticks+1)

    print(totalMinOps)


