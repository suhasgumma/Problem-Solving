def solve(a, b, n):
    res = 0

    while a <=n and b<= n:
        if a < b: a+= b

        else: b+= a

        res+=1
    

    return res


t = int(input())

for _ in range(t):

    a, b, n = map(int, input().split())

    print(solve(a, b, n))