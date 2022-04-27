t = int(input())

for _ in range(t):
    n, q = map(int, input().split())

    arr = list(map(int, input().split()))

    res = arr[0]

    for i in range(1, n):
        res+= max(0, arr[i]- arr[i-1])
    
    print(res)