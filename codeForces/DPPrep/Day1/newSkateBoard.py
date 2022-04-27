def solve(num):
    res = 0

    l = len(num)

    for n in num:
        if int(n)% 4 == 0: res+=1
    
    for i in range(l-1):
        l2 = num[i]+ num[i+1]

        if int(l2)%4 == 0: res+=(i+1)
    

    return res

num = input()

print(solve(num))
