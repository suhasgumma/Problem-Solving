def solve():
    n = int(input())

    q = n//2020

    rem = n - (q*2020)

    if q>= rem:
        print("YES")
    else: print("NO")


t = int(input())

for _ in range(t):
    solve()