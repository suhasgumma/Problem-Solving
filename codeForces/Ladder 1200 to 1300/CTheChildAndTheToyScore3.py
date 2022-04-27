n, m = map(int,input().split())

e = list(map(int, input().split()))

res = 0

for _ in range(m):
    u,v = map(int, input().split())

    res+= min(e[u-1], e[v-1])


print(res)