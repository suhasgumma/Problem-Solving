def solve():
    n = int(input())

    r = input()

    res = 0

    curr = 1

    prev = 0

    while curr < n:
        if r[curr] == r[prev]: res+=1
        
        else: prev = curr

        curr+=1
    

    print(res)

    return


solve()