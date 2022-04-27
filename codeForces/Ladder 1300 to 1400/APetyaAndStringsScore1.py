def solve():
    fS = input()

    sS = input()

    for i in range(len(fS)):
        f = ord(fS[i])
        s = ord(sS[i])

        if f < 97: f+= 32

        if s < 97: s+= 32

        if f < s:
            print(-1)
            return
        
        if f > s:
            print(1)
            return
    

    print(0)
    return


solve()