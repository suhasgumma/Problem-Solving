def solve():
    n = int(input())

    r = list(map(int, input().split()))

    m = int(input())

    b = list(map(int, input().split()))

    res = 0

    prev = 0

    maxim = 0

    for el in r:
        prev+= el
        maxim = max(maxim, prev)
    
    res+= maxim

    prev = 0

    maxim = 0

    for el in b:
        prev+= el
        maxim = max(maxim, prev)
    
    res+= maxim

    print(res)

    return

t = int(input())

# a,b = map(int, input().split())

# arr = list(map(int, input().split()))

for _ in range(t):
    solve()