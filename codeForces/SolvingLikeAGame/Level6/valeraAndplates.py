n, b, p = map(int, input().split())

arr = list(map(int, input().split()))

res = 0

for i in arr:
    if i == 1:
        if b > 0: b-=1

        else: res+=1
    
    if i == 2:
        if p > 0: p-=1

        elif b > 0: b-=1

        else: res+=1


print(res)