s = input()

res = 0

while len(s) > 1:
    summ = 0

    for i in s:
        summ+= int(i)
    
    s = str(summ)

    res+=1

print(res)
