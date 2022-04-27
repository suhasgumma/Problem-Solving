def lcs(str1, str2, l1, l2):
    dp = [[-1 for _ in range(l2+1)] for _ in range(l1+1)]

    for i in range(l1+1):
        for j in range(l2+1):
            if i == 0 or j== 0:
                dp[i][j] = 0
                continue
            
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1+ dp[i-1][j-1]
                continue

            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp


lcss=  []

def getLcss(str1, str2, m, n, string, dp):
    if m == 0 or n==0:
        lcss.append(string)
        return
    
    if str1[m-1] == str2[n-1]:
        string+= str1[m-1]
        return getLcss(str1, str2, m-1, n-1,string, dp)
    
    top = dp[m-1][n]
    left = dp[m][n-1]

    if left>= top:
        getLcss(str1, str2, m, n-1,string, dp)
    
    if top>= left:
        getLcss(str1, str2, m-1,n,string,dp)
    
    return



str1 = "ABCBDAB"
str2 = "BDCABA"
dp = lcs(str1, str2, 7, 6)

getLcss(str1, str2, 7, 6,"",dp)

print(lcss)

# print(lcs("ABCBDAB", "BDCABA", 7, 6))