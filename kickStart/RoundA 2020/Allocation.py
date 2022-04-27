t = int(input())

for i in range(t):

    n, b = map(int, input().split())

    arr = list(map(int, input().split()))

    arr = sorted(arr)

    res, curr = 0, 0
    for el in arr:
        curr+= el
        if curr <= b: res+=1

        else: break
    
    print("Case #"+ str(i+1)+ ": " + str(res))