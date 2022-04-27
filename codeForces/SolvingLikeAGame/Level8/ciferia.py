k = int(input())

l = int(input())

res = 0

gone = False

while l > 1 and not gone:
    if l %k != 0:
        gone = True
    else:
        l/=k
        res+=1


if gone:
    print("NO")

else:
    print("YES")

    print(res-1)