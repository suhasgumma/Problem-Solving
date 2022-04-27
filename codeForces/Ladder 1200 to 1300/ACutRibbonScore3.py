def cutRibbonDp(n, a,b,c):
    dp = [0 for _ in range(n+1)]

    for i in range(1,n+1):
        res1, res2, res3 = -1, -1, -1

        if i-a >= 0: res1 = dp[i-a]

        if i-b >=0: res2 = dp[i-b]

        if i-c >= 0: res3 = dp[i-c]

        finRes = max(res1, res2, res3)

        if finRes < 0: dp[i] = -1

        else: dp[i] = 1+ finRes
    
    # print(dp)

    return dp[n]



n, a, b, c = map(int, input().split())

print(cutRibbonDp(n, a, b, c))

    