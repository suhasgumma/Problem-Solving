def solve(n):
    res = n
    for i in range(n-1, -1, -1):
        res = res and i

        if res == 0: return i

    return

t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    solve()