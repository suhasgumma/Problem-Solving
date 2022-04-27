n = int(input())

arr = list(map(int, input().split()))

res = min(arr[0], arr[n-1])

for i in range(1, n-1):
    maxi = max(arr[i], arr[i+1])

    res = min(res, maxi)


print(res)