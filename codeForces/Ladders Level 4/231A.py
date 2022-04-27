def solve():
    n = int(input())

    res = 0

    for i in range(n):
        cnt = 0

        arr = list(map(int, input().split()))

        for i in arr:
            if i == 1: cnt+=1
        
        if cnt > 1: res+=1
    

    print(res)
    return


solve()