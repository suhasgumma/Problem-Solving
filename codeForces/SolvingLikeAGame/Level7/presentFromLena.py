n = int(input())

total  = (2*n) + 1

mid = total//2

arr = [' '] * total

for i in range(mid+1):
    arr[mid] = i

    for j in range(i):
        arr[mid-j-1] = i-j-1

        arr[mid+j+1] = i- j- 1
    

    res = ''

    firstLetter = False

    for i in arr:
        if i == " " and not firstLetter: 
            res+= "  "
        
        elif i != " ":
            res+= (str(i) + " ")
            firstLetter = True
    
    print(res[:-1])

for i in range(mid-1, -1, -1):
    arr = [' '] * total
    arr[mid] = i

    for j in range(i):
        arr[mid-j-1] = i-j-1

        arr[mid+j+1] = i- j- 1
    

    res = ''

    firstLetter = False

    for i in arr:
        if i == " " and not firstLetter: 
            res+= "  "
        
        elif i != " ":
            res+= (str(i) + " ")
            firstLetter = True
    
    print(res[:-1])
