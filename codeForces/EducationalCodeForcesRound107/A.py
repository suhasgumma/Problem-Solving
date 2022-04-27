t = int(input())

for _ in range(t):
    n = int(input())

    voters = list(map(int, input().split()))

    res = 0

    for v in voters:
        if v != 2: res+=1
    
    print(res)