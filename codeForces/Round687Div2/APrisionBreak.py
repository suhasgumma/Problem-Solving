t = int(input())

for _ in range(t):
    n, m, r, c = map(int, input().split())

    edges = [(1, m), (n, 1), (n, m)]

    res = r+ c -2
    for edge in edges:
        dist = abs(r- edge[0]) + abs(c- edge[1])

        res = max(res, dist)
    
    print(res)