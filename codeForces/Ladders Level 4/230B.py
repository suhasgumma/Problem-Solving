import math

def sieve(n):
    sieveArray = [True for _ in range(n+1)]

    for i in range(2, n+1):
        if sieveArray[i]:
            for j in range(2*i, n+1, i):
                sieveArray[j] = False
    

    return sieveArray

def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    maxim = max(arr)

    mSRoot = math.ceil(math.sqrt(maxim))

    sieveArray = sieve(mSRoot)

    for i in arr:
        sRoot = math.sqrt(i)

        if i == 1:
            print("NO")
        elif sRoot == math.floor(sRoot) and sieveArray[int(sRoot)]:
            print("YES")
        
        else: print("NO")
    
    return

solve()