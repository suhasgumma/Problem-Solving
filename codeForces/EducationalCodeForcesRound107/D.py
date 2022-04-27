def allEmpty(poss):
    for i in poss:
        if len(i) != 0: return False
    
    return True

def solve(n, k):
    allL = [i for i in range(k)]

    poss = [set(allL) for _ in range(k)]

    res = 'aa'

    poss[0].remove(0)

    while not allEmpty(poss):
        curr = ord(res[-1]) - 97

        maxC = None
        maxL = 0

        for i in poss[curr]:
            if len(poss[i]) > maxL:
                maxL = len(poss[i])
                maxC = i

        poss[curr].remove(maxC)

        res+= chr(97 + maxC)

        print(res)
        print(poss)
    
    return res


print(solve(2, 4))