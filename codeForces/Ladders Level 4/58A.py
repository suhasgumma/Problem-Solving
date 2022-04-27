def solve():
    word = input()

    n = len(word)

    h, e, l, o = -1, -1, -1, -1


    for i in range(n):
        if word[i] == 'h':
            h = i
            break
    
    if h == -1:
        print("NO")
        return
    
    for i in range(h+1, n):
        if word[i] == 'e':
            e = i
            break
    
    if e == -1:
        print("NO")
        return
    

    for i in range(e+1, n):
        if word[i] == 'l':
            l = i
            break
    
    if l == -1:
        print("NO")
        return

    lBool = False

    for i in range(l+1, n):
        if word[i] == 'l':
            l = i
            lBool = True
            break
    
    if not lBool:
        print("NO")
        return
    

    for i in range(l+1, n):
        if word[i] == 'o':
            o = i
            break
    
    if o == -1:
        print("NO")
        return

    
    print("YES")


solve()


