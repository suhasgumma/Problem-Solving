def solve():
    y, k, n = map(int, input().split())


    res = []
    

    start = y//k

    if (k*start)-y <=0: start+=1

    end = n//k

    if (k *end)-y > n: end-=1

    if start > end:
        print(-1)
        return
    

    for x in range(start, end+1):
        res.append((k*x)-y)
    print(*res)



solve()