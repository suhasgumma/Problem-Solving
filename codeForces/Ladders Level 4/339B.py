def solve():
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    res = arr[0] - 1


    for i in range(1, m):
        diff = arr[i] -  arr[i-1]

        if diff >= 0: res+= diff

        else: res+= (n+diff)
    

    print(res)

    return


solve()