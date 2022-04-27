t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    kSquare = k* k

    den = (kSquare+1) * (k+1)

    n1 = n//den

    res = [n1]*4

    for i in range(1, 4):
        res[i] = res[i-1] * k
    

    print(*res)