import math

def reqSteps(s, g):
    oS = ord(s)
    oG = ord(g)

    diff = abs(oS- oG)

    return min(diff, 26-diff)


n = int(input())

string = input()

genome = 'ACTG'

res = math.inf

for i in range(n-3):
    curr = string[i:i+4]

    currMin = 0

    for j in range(4):
        currMin+= (reqSteps(curr[j], genome[j]))
    
    res = min(res, currMin)


print(res)