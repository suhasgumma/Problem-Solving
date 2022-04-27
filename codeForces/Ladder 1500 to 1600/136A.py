def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    resArray = [0 for _ in range(n)]

    for i in range(n):
        resArray[arr[i]-1] = i+1
    

    print(*resArray)

    return


solve()