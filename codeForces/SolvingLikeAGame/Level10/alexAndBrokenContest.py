def solve(string):

    n = len(string)

    count = 0

    i = 0

    while i <= n-5:
        subStr = string[i: i+5]

        if subStr== "Danil" or subStr == "Slava":
            count+=1
            i+=5
        
        else: i+=1
    
    i = 0
    while i <= n-6:
        subStr = string[i: i+6]

        if subStr== "Nikita":
            count+=1
            i+=6
        
        else: i+=1
    
    i = 0
    while i <= n-4:
        subStr = string[i: i+4]

        if subStr== "Olya":
            count+=1
            i+=4
        
        else: i+=1
    
    i = 0
    while i <= n-3:
        subStr = string[i: i+3]

        if subStr== "Ann":
            count+=1
            i+=3
        
        else: i+=1
    


    if count== 1: return "YES"

    return "NO"



string = input()

print(solve(string))