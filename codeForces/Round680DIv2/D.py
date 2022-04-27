import math
def getPrimeFactors(n):
    res = []

    if n%2 == 0:
        res.append(2)
        n = n//2
    
    while n%2 == 0:
        n = n//2

    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i== 0:
            res.append(i)
            n = n//i
        
        while n % i== 0: n= n//i

    if n> 2: res.append(n)

    return res


def solve(p, q):
    if p %q != 0: return p

    qfacts = getPrimeFactors(q)

    # print(qfacts)

    for f in qfacts:
        newP = p//f

        if p%f == 0 and newP %q != 0: return newP
    
    if q == 2: return 1

    for i in range(qfacts[-1],p):
        newP = p//i
        if p%i == 0 and newP %i != 0: return newP
    

t = int(input())

for _ in range(t):
    p, q = map(int, input().split())

    print(solve(p, q))
