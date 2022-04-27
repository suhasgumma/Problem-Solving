import math

def factorial(n):
    res = 1

    for i in range(2, n+1): res*=i

    return res


def ncx(n,x):
    nfactorial = factorial(n)

    nMinXFactorial = factorial(n-x)


    return nfactorial//(nMinXFactorial)


def solve(n, x, pos):

    midsG = 0
    midsL = 0

    mid = n//2

    if mid == pos: return factorial(n-1)

    left = 0
    right = n

    while mid != pos0:
        print(mid)
        if mid > pos:
            midsG+=1
            right = mid
            mid = (left+mid)//2
            
        
        else:
            midsL+=1
            left = mid
            mid = (mid+right)//2
            
    

    elGx = n- x

    elLs = x-1

    print(midsG, midsL, elGx, elLs)

    # midsG+=1
    # midsL+=1

    rem = n- midsG-midsL-1

    print(rem)

    res = ncx(elLs, midsL) * ncx(elGx, midsG)* factorial(rem)

    return res%((math.pow(10, 9))+7)




n, x, pos = map(int, input().split())

res = solve(n,x, pos)

print(res)