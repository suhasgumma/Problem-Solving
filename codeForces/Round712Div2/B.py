def equalZeroes(a, b):
    aCount = 0
    bCount = 0
    for i in a: 
        if i == '0': aCount+=1

    for i in b:
        if i == '0': bCount+=1
    
    return aCount == bCount
    


def isPoss(a, b, n):

    if not equalZeroes(a, b): return "NO"

    zeroList = [0 for _ in range(n)]
    oneList = [0 for _ in range(n)]

    if a[0] == '0':
        zeroList[0] = 1
    
    else: oneList[0] = 1

    for i in range(1, n):
        if a[i] == '0':
            zeroList[i] = 1+ zeroList[i-1]
            oneList[i] = oneList[i-1]
        
        else:
            zeroList[i] = zeroList[i-1]
            oneList[i]= 1+ oneList[i-1]
    
    
    
    flipSet = set()

    

    for i in range(n):
        if oneList[i] == zeroList[i]:
            flipSet.add(i)

    # print(flipSet)
    

    if a[0] == b[0]: match = 1
    else: match = 0

    for i in range(1, n):

        check = (match == 0 and a[i] == b[i]) or (match == 1 and a[i] != b[i])

        if match == 0 and a[i] == b[i]: match = 1

        if match == 1 and a[i] != b[i]: match = 0

        

        if check:
            # print(i)
            if i-1 not in flipSet: return "NO"
    

    return "YES"


t = int(input())

for _ in range(t):
    n = int(input())

    a = input()
    b = input()

    print(isPoss(a, b, n))