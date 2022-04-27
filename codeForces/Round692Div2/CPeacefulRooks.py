def solve(n,m, rooks):
    rows = set()
    cols = set()

    for rook in rooks:
        rows.add(rook[0])
        cols.add(rook[1])
    
    rem = n-m
    
    res = 0
    cons = 0

    oc = 0
    for rook in rooks:
        x,y = rook[0], rook[1]

        if x == y: continue

        rows.remove(x)
        cols.remove(y)

        
        
        if x in cols and y in rows:
            res+=2
            cons+=1
            

        elif x not in cols:
            res+=1
            oc+=1
            rows.add(x)
            cols.add(x)
        
        else:
            res+=1
            oc+=1
            rows.add(y)
            cols.add(y)
    

    if rem > cons: return res

    used = cons - rem

    if used< oc:
        res+= used


    
    return res


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    rooks = []
    for _ in range(m):
        x, y = map(int, input().split())

        rooks.append((x,y))
    
    print(solve(n, m, rooks))