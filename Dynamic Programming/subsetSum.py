#An array is given and u have to find the subset with the given sum.

#Recursion
def recursion(subset, sum, size):

    #Base Cases
    if sum == 0:
        return True
    
    if size == 0:
        return False

    #Choice Diagram

    if subset[size-1] > sum:
        return recursion(subset, sum, size-1)
    
    if subset[size-1] <= sum:
        bool1 = recursion(subset, sum, size-1)
        bool2 =  recursion(subset, sum - subset[size-1], size-1)

        return bool1 or bool2


def tabulation(subset, sum, size):
    dp = [[0 for _ in range(sum+1)] for _ in range(size+1)]

    print(len(dp), len(dp[0]))

    for i in range(size+1):
        for j in range(sum+1):
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            
            elif subset[i-1] > j:
                dp[i][j] = dp[i-1][j]
            
            elif subset[i-1] <= j:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j - subset[i-1]])
    

    return dp[size][sum]


print(tabulation([1,3,8,5,99995], 100000, 5))
print(recursion([1,3,8,5,99995], 100000, 5))


            


    