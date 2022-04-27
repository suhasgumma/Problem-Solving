def getPow2(num):
    start = num
    res = 0

    while(start > 1):
        res+=1
        start = start//2
    
    return res

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ansDict = {}

    for i in arr:
        pow2 = getPow2(i)

        if pow2 in ansDict: ansDict[pow2]+=1

        else: ansDict[pow2] = 1

    res = 0
    
    for i in ansDict:
        n = ansDict[i]

        res+= ((n*(n-1))//2)
    
    print(res)
