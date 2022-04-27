def solve():
    luckyNums = [4, 44, 444, 7, 77, 777, 47, 74, 447, 474, 744, 477, 747, 774]

    n = int(input())

    for i in luckyNums:
        if n%i == 0:
            print("YES")
            return
    

    print("NO")
    return


solve()