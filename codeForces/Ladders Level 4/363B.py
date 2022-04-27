def solve():
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    dpArr = [arr[0] for _ in range(n) ]

    for i in range(1, n):
        dpArr[i] = arr[i]+ dpArr[i-1]
    

    minWidth = dpArr[k-1]
    minIdx = 0

    for i in range(k, n):
        currWidth = dpArr[i]- dpArr[i-k]

        if currWidth < minWidth:
            minWidth = currWidth
            minIdx = i-k+1
    

    print(minIdx+1)

    return


solve()