def solve():

    s = input()

    n = len(s)

    prev = None

    count = 0

    for p in s:
        if p == prev:
            count+=1
        
        else:
            if count >= 7:
                print("YES")
                return
            prev = p
            count = 1
    

    if count >=7:
        print("YES")
        return
    

    print("NO")
    return


solve()