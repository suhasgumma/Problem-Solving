def solve(mat, n, m):
    res = 0

    dp = [[1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if mat[i][j] == '.': dp[i][j] = 0

    
    for i in range(n-2, -1, -1):
        for j in range(1, m-1):

            if dp[i][j] == 0: continue
            
            minh = min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])

            dp[i][j] = 1+ minh
    

    for i in range(n):
        for j in range(m):
            res+= dp[i][j]
    

            
    return res


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    mat = []

    for _ in range(n):
        row = input()
        mat.append(row)
    
    print(solve(mat, n, m))

