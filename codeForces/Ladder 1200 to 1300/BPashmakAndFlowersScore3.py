def solve(arr, n):
    arr = sorted(arr)

    maxDiff = arr[n-1] - arr[0]

    if maxDiff == 0:
        possC = n*(n-1)//2
        return maxDiff, possC

    leftC, rightC = 0, 0

    left = 0

    while arr[left] == arr[0]:
        leftC+=1
        left+=1
    
    right = n-1

    while arr[right] == arr[n-1]:
        rightC+=1
        right-=1
    
    possC = leftC*rightC

    return maxDiff, possC


n = int(input())

arr = list(map(int, input().split()))

print(*solve(arr, n))