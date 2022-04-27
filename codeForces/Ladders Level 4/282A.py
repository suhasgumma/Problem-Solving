def solve():
    poss1 = "++X"
    poss2 = "X++"
    poss3 = "X--"
    poss4 = "--X"

    res = 0

    n = int(input())

    for _ in range(n):
        op = input()

        if op == poss1 or op == poss2: res+=1

        else: res-=1
    

    print(res)

    return


solve()