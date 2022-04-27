import math

fMinEnd, sMinEnd = math.inf, math.inf

fMaxStart, sMaxStart = 0, 0

n = int(input())

for _ in range(n):
    s, e = map(int, input().split())

    fMinEnd = min(fMinEnd, e)
    fMaxStart = max(fMaxStart, s)


m = int(input())

for _ in range(m):
    s, e = map(int, input().split())

    sMinEnd = min(sMinEnd, e)
    sMaxStart = max(sMaxStart, s)


res1 = max(0, sMaxStart -fMinEnd)

res2 = max(0,fMaxStart- sMinEnd)

print(max(res1, res2))


