import math

def floorNumber(n, x):
    if n<=2: return 1

    res = math.ceil((n-2)/x)

    return res+1


t = int(input())

for _ in range(t):
    n,x = map(int, input().split())

    print(floorNumber(n,x))