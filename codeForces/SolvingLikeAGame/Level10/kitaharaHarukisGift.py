def solve(arr,n):
    tot = sum(arr)

    if tot % 200 != 0: return "NO"

    hund = 0
    twoHund = 0

    for i in arr:
        if i == 100: hund+=1

        else: twoHund+=1
    
    half = tot//2

    if twoHund%2 != 0 and hund< 2: return "NO"

    return "YES"
    



n = int(input())

arr = list(map(int,input().split()))

print(solve(arr,n))
