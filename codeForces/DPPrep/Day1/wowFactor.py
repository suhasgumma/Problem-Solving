def solve(string):
    n = len(string)

    dp = [0]* n

    for i in range(1, n):
        if string[i]== "v" and string[i-1] == "v": dp[i] = dp[i-1]+1

        else: dp[i] = dp[i-1]
    
    res= 0

    for i in range(n):
        if string[i] == "o":
            left = dp[i]
            right = dp[n-1]- dp[i]

            res+= (left*right)
    

    return res


string = input()

print(solve(string))