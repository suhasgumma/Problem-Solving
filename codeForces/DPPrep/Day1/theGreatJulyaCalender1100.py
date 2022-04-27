def greatestDigit(n):
    res = 0

    while n > 0:
        res = max(res, n%10)
        n = n//10
    

    return res

def solve(magicNum):
    if magicNum == 0: return 0

    res = 0

    while magicNum > 0:
        maxDig = greatestDigit(magicNum)
        magicNum-= maxDig
        res+=1
    
    return res


magicNum = int(input())

print(solve(magicNum))