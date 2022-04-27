def binSearch(arr, left, right, el):
    while left < right:
        mid = (left+right)//2

        if arr[mid] == el: return mid

        if arr[mid] > el: right = mid-1

        else: left = mid+1
    

    if arr[left] == el: return left

    if arr[left] > el: return left-1

    return left


def solve(arr, n, t):
    res = 0

    dpArr = [arr[0]]* n

    for i in range(1, n):
        dpArr[i] =  arr[i]+ dpArr[i-1]

    for i in range(n):
        if i == 0: el = t

        else: el = t+ dpArr[i-1]

        j = binSearch(dpArr, i, n-1, el)

        res = max(res, j-i+1)
    

    return res


n, t = map(int, input().split())

arr = list(map(int, input().split()))

print(solve(arr, n, t))

