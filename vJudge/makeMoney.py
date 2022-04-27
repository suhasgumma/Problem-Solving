def solve(arr, n):
    res = -float('inf')

    count = 1

    curr = 1

    while curr < n:
        if arr[curr] >= arr[curr-1]: count+=1

        else:
            res = max(count, res)
            count = 1
        
        curr+=1
    
    res = max(res, count)
    

    return res


n = int(input())

arr = list(map(int, input().split()))

print(solve(arr, n))
