def solve():
    n, d = map(int, input().split())

    arr = list(map(int, input().split()))

    allGood = True

    for i in arr:
        if i > d: allGood = False

    if allGood:
        print("YES")
        return

    for i in range(n):
        for j in range(i+1, n):
            if arr[i]+ arr[j] <= d:
                print("YES")
                return
    
    print("NO")

    return


t = int(input())




for _ in range(t):
    solve()