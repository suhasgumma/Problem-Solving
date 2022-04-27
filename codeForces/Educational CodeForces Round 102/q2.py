#By recursion


def rec(n, prev, start, dur, volume):
    #Must Return max possible volume

    #Base Case

    if n == 0: return 0

    if prev == 0: return 0

    ch1, ch2 = 0, 0

    #Choice 1 take it if available

    curr = start[n-1]+ dur[n-1]

    if curr < prev:
        newPrev = start[n-1]
        ch1 = volume[n-1]+ rec(n-1, newPrev, start, dur, volume)
    
    ch2 = rec(n-1, prev, start, dur, volume)

    return max(ch1, ch2)



#Bottom up

def bottomUp(start, duration, volume):

    n = len(start)

    maxEndTime = 0

    for i in range(n):
        eT = start[i] + duration[i]
        maxEndTime = max(maxEndTime, eT)

    maxS = maxEndTime+1

    dp = [[0 for _ in range(maxS+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(maxS+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
                continue

            curr = start[i-1] + duration[i-1]

            op1, op2 = 0, 0

            if curr < j:
                newJ = start[i-1]
                op1 = volume[i-1]+ dp[i-1][newJ]
            
            op2 = dp[i-1][j]

            dp[i][j] = max(op1, op2)
    

    return dp[n][maxS]



start = [10, 5, 15, 18, 30]
dur = [30, 12, 20, 35, 35]
vol = [50, 51, 20, 25, 10]

print(bottomUp(start, dur, vol))

