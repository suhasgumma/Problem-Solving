t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    s = 'abc'

    rem  = n

    res = ''
    i = 0
    while rem > 0:
        res+= (s[i]*k)

        rem-= k

        if i == 2: i = 0

        else: i+=1
    

    print(res[:n])
