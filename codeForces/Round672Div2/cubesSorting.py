def completelyReverse(arr, n):
    for i in range(1, n):
        if arr[i] >= arr[i-1]: return "YES"
    
    return "NO"


t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    print(completelyReverse(arr, n))