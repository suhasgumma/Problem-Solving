res = 0

for i in range(1000):
    if i%3 == 0:
        res+= i
    
    elif i %5 ==0:
        res+= i


print(res)