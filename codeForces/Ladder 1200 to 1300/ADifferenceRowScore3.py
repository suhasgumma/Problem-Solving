n = int(input())

arr = list(map(int, input().split()))

arr = sorted(arr)

arr[0], arr[n-1] = arr[n-1],arr[0]

print(*arr)