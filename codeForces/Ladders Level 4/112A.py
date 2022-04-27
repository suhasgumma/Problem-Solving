def solve():
    str1 = input()
    str2 = input()

    n = len(str1)

    for i in range(n):
        ord1 = ord(str1[i])
        ord2 = ord(str2[i])

        if ord1 < 97: ord1+= 32

        if ord2 < 97: ord2+= 32

        if ord1 < ord2:
            print(-1)
            return
        
        if ord2 < ord1:
            print(1)
            return
    

    print(0)
    return

solve()