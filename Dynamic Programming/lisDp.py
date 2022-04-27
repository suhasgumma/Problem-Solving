

def lisDp(array, size):
    dp = [0 for _ in range(size)]

    dp[0] = 1
    for i in range(1, size):
        maxi = 0
        for j in range(i):
            if array[i] >= array[j]:
                maxi = max(maxi, dp[j])
        dp[i] = maxi+1
    
    return dp


print(lisDp([-1, 3,4, 5,2,2], 6))

