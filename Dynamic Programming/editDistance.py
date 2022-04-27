def editDistance(str1, str2, m, n):
    #Base Case
    if m == 0 or n==0:
        return m+n
    
    if str1[m-1] != str2[n-1]:
        return 1+ min(editDistance(str1, str2, m, n-1), editDistance(str1, str2, m-1, n-1))
    
    return editDistance(str1, str2, m-1, n-1)


def editDistDp(str1, str2, m,n):
    dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = i+j
                continue
            if str1[i-1] != str2[j-1]:
                dp[i][j] = 1+ min(dp[i-1][j], dp[i-1][j-1])
            else:
                dp[i][j] = dp[i-1][j-1]
    
    return dp[m][n]


print(editDistDp("kitten", "sitting", 6,7))