import math

def minStepsForANumber(arr, n):
    res = 0

    for i in arr:
        if i > n:
            res+= (i-n-1)
        
        if i < n:
            res+= (n-i-1)
    
    return res

n = int(input())
arr = list(map(int,input().split()))

minT = None

minSteps = math.inf

for i in range(1,101):
    stepsReq = minStepsForANumber(arr, i)

    if stepsReq < minSteps:
        minT = i
        minSteps = stepsReq

print(minT, minSteps)