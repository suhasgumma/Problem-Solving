t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    diff = x-y

    if diff == 1: print("NO")

    else: print("YES")