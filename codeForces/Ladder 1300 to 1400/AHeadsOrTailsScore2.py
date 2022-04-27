def solve():
    x, y, a,b = map(int, input().split())

    newA = a

    res = []

    while newA <= x:
        newB = b

        while newB<=y and newB < newA:
            res.append((newA, newB))
            newB+=1
        
        newA+=1
    

    n = len(res)

    print(n)

    for x, y in res:
        print(x, y)
    
    return


solve()