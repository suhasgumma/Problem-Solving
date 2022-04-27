def reOrder(arr):
    resArray = []

    arr =sorted(arr)

    mid = len(arr)//2

    i = 0
    j = mid

    while i< mid and j < len(arr):
        resArray.append(arr[j])
        resArray.append(arr[i])
        i+=1
        j+=1
    
    while j < len(arr):
        resArray.append(arr[j])
        j+=1
    
    return resArray


n = int(input())

arr = list(map(int, input().split()))

resArray = reOrder(arr)

res = (n//2)+ (n%2-1)

print(res)

print(*resArray)