n = int(input())

profs = list(map(int, input().split()))

res = []

currTotal = 0

currNegs = 0

for prof in profs:
    if prof>= 0:
        currTotal+=1
    
    else:
        if currNegs == 2:
            res.append(currTotal)
            currTotal = 1
            currNegs = 1
        else:
            currNegs+=1
            currTotal+=1


res.append(currTotal)

print(len(res))

print(*res)