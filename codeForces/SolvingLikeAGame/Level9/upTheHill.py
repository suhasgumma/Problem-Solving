up = int(input())

down = int(input())

maxim = up+down+1

res = []

if up > down:
    res.append(1)

    curr = maxim - up + 1

    downCurr = curr-1

    while curr <= maxim:
        res.append(curr)
        curr+=1
    

    while downCurr > 1:
        res.append(downCurr)
        downCurr-=1

else:
    res.append(maxim)
    
    curr = maxim-up-1

    upCurr = curr+1

    while curr>= 1:
        res.append(curr)
        curr-=1
    
    while upCurr < maxim:
        res.append(upCurr)
        upCurr+=1
    


print(*res)