n = int(input())

domino = input()

currLetter = None

prev = 0

res = 0

for i in range(n):
    if domino[i]== "L":
        count = i-prev+1
        
        if currLetter == "R":
            if count%2 != 0: count-=1
        
        res+= count

        prev = i
        currLetter = "L"
    
    if domino[i] == "R":
        if currLetter == "R":
            res+=(i-prev+1)

            print(res)
        
        else: currLetter = "R"

        prev = i

if currLetter == "R":
    res+= (n-prev)


print(n-res)