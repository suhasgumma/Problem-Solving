def solve():
    n = int(input())

    b = input()

    prev = -1

    res = ''

    for curr in b:

        if curr == '0':
            if prev == 1:
                res+= '0'
                prev = 0
            
            else:
                res+='1'
                prev = 1
        
        else:
            if prev == 2:
                res+= '0'
                prev = 1
            
            else:
                res+='1'
                prev = 2
    
    print(res)

    return


t = int(input())




for _ in range(t):
    solve()