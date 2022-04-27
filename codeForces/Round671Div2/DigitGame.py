def digitGame(string):
    n = len(string)

    if n%2 == 0:
        for i in range(1, n, 2):
            digit = int(string[i])

            if digit%2 == 0: return 2
        
        return 1
    
    else:
        for i in range(0, n, 2):
            digit = int(string[i])

            if digit%2 != 0: return 1
        
        return 2

t = int(input())

for _ in range(t):
    n = int(input())
    number = input()

    print(digitGame(number))
    

