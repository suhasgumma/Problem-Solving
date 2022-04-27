# n -(n%k) - (k//2)

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    remAfterEqualDist = n%k

    lim = k//2

    rem = remAfterEqualDist - lim

    if rem <0: rem = 0

    res = n-rem

    print(res)