t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    botArray = list(map(int, input().split()))

    botSet = set(botArray)

    leftArr = list(map(int, input().split()))

    res = 0

    for i in leftArr:
        if i in botSet: res+=1
    
    print(res)