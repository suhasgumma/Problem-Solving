def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    arr = sorted(arr)

    res = 0

    for i in range(1, n+1):
        curr = arr[i-1]

        need = abs(curr-i)

        res+= need
    

    print(res)
    return


solve()