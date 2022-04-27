import math

def solve():
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    arr = sorted(arr)

    i = 0

    j = n-1


    res = math.inf
    while j < m:

        currDiff = arr[j]- arr[i]

        res = min(res, currDiff)

        i+=1
        j+=1
    
    print(res)
    return


solve()
