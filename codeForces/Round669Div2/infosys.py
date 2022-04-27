def lcs(str1, str2):
    l1= len(str1)
    l2 = len(str2)
    dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
    for i in range(l1+1):
        for j in range(l2+1):
            if i == 0 or j == 0: continue

            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            
            else:
                ch1 = dp[i-1][j]
                ch2 = dp[i][j-1]

                dp[i][j] = max(ch1, ch2) 
    i = l1
    j = l2

    res = ''

    while i>0 and j>0:
        if str1[i-1] == str2[j-1]:
            res+= str1[i-1]
            i-=1
            j-=1
        
        else:
            ch1 = dp[i-1][j]
            ch2 = dp[i][j-1] 

            if ch1 > ch2:
                i = i-1
            else:
                j-=1
    
    return res

def rev(string):
    res = ''
    for i in range(len(string)-1, -1, -1): res+= string[i]

    return res


string = 'babad'
str2 = ''

res = lcs(string, rev(string))

print(res)

