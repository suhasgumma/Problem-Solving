import math

def solve():
    n, k = map(int, input().split())

    oddBoundary=  math.ceil(n/2)

    # k = int(input())

    if k <= oddBoundary:
        res = (2*k)-1
    
    else:
        newK = k- oddBoundary

        res = 2* newK
    
    print(res)

    return


solve()
