t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    indImpact = [0] * n

    summ = sum(arr)

    target = summ//n

    indImpact[0] = target- arr[0]

    for i in range(1, n):
        indImpact[i] = target- arr[i]+ indImpact[i-1]
    
    compImpact = [0] * n

    for i in range(n): compImpact[i] = indImpact[i]* (n-i)

    maxIndex= 0

    for i in range(1,n):
        if compImpact[i] > compImpact[maxIndex]:
            maxIndex = i

    print(indImpact)

    print(compImpact)
        
    maxImpact = indImpact[maxIndex]

    for i in range(maxIndex, n):
        indImpact[i]-= maxImpact
    
    res = sum(indImpact)

    print(res)