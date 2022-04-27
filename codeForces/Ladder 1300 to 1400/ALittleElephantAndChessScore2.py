def solve():

    falseFound = False
    for _ in range(8):
        r = input()

        if r != "WBWBWBWB" and r!= "BWBWBWBW": falseFound = True
    

    if falseFound:
        print("NO")
        return
    print("YES")
    return


solve()