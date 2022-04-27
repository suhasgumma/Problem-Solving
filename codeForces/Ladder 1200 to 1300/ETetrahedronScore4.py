def solveDp(n):
    dp = [[0 for _ in range(4)] for _ in range(n+1)]

    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(4):
            res = 0

            for k in range(4):
                if k == j: continue

                res+= dp[i-1][k]
            
            dp[i][j] = res
    

    res = dp[n][0]

    for i in range(n):
        print(dp[i][0])

    return res % 1000000007


n = int(input())

print(solveDp(n))

