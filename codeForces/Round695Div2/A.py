import math

def solve():
    # n, m = map(int(input()))

    # arr = list(map(int, input().split()))

    n = int(input())

    res = '0123456789'

    if n == 1:
        print('9')
        return
    
    if n == 2:
        print("98")
        return
    
    if n == 3:
        print(989)
        return
    
    rem = n-3

    q = math.ceil(rem/10)

    res = res* q

    res = '989'+ res[:rem]

    print(res)

    return
    

    return


t = int(input())




for _ in range(t):
    solve()


#solve()