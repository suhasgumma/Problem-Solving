t = int(input())

for _ in range(t):
    n = int(input())

    h = list(map(int, input().split()))

    odds, evens = [], []

    for i in h:
        if i % 2 == 0:
            evens.append(i)
        
        else: odds.append(i)
    
    for i in evens: odds.append(i)

    print(*odds)