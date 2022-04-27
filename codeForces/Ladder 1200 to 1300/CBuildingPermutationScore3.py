n = int(input())

arr = list(map(int, input().split()))

arr = sorted(arr)

res = 0

for i in range(n):
    el = arr[i]

    res+= (abs(el-i-1))


print(res)