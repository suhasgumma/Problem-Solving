def solve(arr, n):
    maxi = max(arr)

    if arr[0] == maxi and arr[0] > arr[1]: return 1

    if arr[n-1] == maxi and arr[n-1] > arr[n-2]: return n

    for i in range(1,n-1):
        if arr[i] == maxi:
            if arr[i] > arr[i-1] or arr[i] > arr[i+1]:
                return i+1
    

    return -1



t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    print(solve(arr, n))