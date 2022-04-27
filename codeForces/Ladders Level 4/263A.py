def solve():
    matrix = []

    for _ in range(5):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                x, y = i, j
    

    res = abs(2-x)+ abs(2-y)

    print(res)
    return


solve()
    

