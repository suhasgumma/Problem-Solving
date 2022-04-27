t = int(input())

for _ in range(t):
    n = int(input())

    s = input()

    res = 0

    i = n-1

    while i >= 0 and s[i]== ')':
        res+=1
        i-=1
    
    rem = n- res

    # print(res, rem)

    if res > rem: print("YES")

    else: print("NO")