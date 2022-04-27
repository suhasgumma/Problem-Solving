def solve(arr,n):
    res = []

    i = 0

    while i <n:
        res.append(-arr[i+1])

        res.append(arr[i])

        i+=2
    

    return res


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    res = solve(arr, n)

    print(*res)