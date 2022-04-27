n = int(input())

variants = list(map(int, input().split()))

res = 0

for i in range(n):
    v = variants[i]

    currRes = (v-1)*(i+1)

    res+=(currRes+1)


print(res)