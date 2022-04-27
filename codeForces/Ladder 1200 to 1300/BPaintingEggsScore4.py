def solve():
    n = int(input())

    A, G = 0, 0


    res = ''
    for _ in range(n):
        a, g = map(int, input().split())

        if abs(A+a-G) <= 500:
            res+= 'A'
            A+=a
        
        elif abs(G+g-A) <= 500:
            res+= 'G'
            G+=g
        
        else:
            print(-1)
            return
        
    
    print(res)

solve()