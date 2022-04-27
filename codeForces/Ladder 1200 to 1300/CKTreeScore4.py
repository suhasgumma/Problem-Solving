def rec(n, k, d, isThere):
    if n == 0:
        if isThere: return 1

        return 0
    
    res = 0

    for i in range(1, k+1):
        if i >= d:
            if n-i>=0: res+= rec(n-i, k, d, True)
        else:
            if n-i>=0: res+= rec(n-i, k, d, isThere)
    
    return res


def solveByDP(n, k, d):
    dp = [[0 for _ in range(2)] for _ in range(n+1)]

    dp[0][0] = 0
    dp[0][1] = 1

    for i in range(1, n+1):
        for b in range(0, 2):
            res = 0
            for j in range(1, min(i,k)+1):
                if j >= d: res+= dp[i-j][1]

                else: res+= dp[i-j][b]
            
            dp[i][b] = res
    
    # print(dp)
    
    return dp[n][0]% 1000000007


def solve(n, k, d):
    
    dp = [0 for _ in range(n+1)]

    dp[0], dp[1] = 1, 1

    for i in range(2, n+1):
        if i <= k:
            dp[i] = 2*dp[i-1]
            continue

        for j in range(1, k+1):
            dp[i]+= dp[i-j]
    

    res = 0

    for i in range(d, k+1):
        req = n- i

        if req<0: break

        res+= dp[req]
    
    # print(dp)
    
    return res


n,k, d = map(int, input().split())

print(solveByDP(n, k, d))

