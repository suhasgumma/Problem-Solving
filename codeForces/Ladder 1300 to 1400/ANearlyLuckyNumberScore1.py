def solve():
    n = input()

    ld = 0

    # print(s)

    for i in n:
        if i == '4' or i == '7': ld+=1
    
    lDs = str(ld)

    # print(lDs)

    for i in lDs:
        if i != '4' and i != '7':
            print("NO")
            return
    

    print("YES")
    return

solve()