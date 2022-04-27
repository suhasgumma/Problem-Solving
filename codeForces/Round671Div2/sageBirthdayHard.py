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


def countPeaks(arr):
    if len(arr)<=2: return 0

    res = 0

    i = 0
    j = i+2

    while j < len(arr):
        left = arr[i]
        right = arr[j]

        middle = arr[i+1]

        if middle< left and middle < right: res+=1

        i+=1
        j+=1

    return res 



n = int(input())

arr = list(map(int, input().split()))

resArray = reOrder(arr)

res = countPeaks(resArray)

print(res)

print(*resArray)