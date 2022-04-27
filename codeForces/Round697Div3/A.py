def solve():

    # n = map(int, input().split())

    n = int(input())

    while n > 1:
        if n%2 == 0: n = n//2

        else:
            print("YES")
            return
    
    print("NO")
    return



t = int(input())

for _ in range(t):
    solve()


# solve()