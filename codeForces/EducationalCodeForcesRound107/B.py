import math

def isPrime(n) :
 
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    if (n % 2 == 0 or n % 3 == 0) :
        return False
 
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
 
    return True


def nextPrime(n):
    i = n+1

    while True:
        if isPrime(i): return i

        i+=1
    

def solve(a, b, c):

    gcd = int('1' * c)
    xa = int('1' * a)
    xb = int('1' * b)

    p = nextPrime((math.ceil(xa/gcd))-1)

    x = gcd * p

    if xa == xb:
        y = gcd* nextPrime(p)
    
    else:
        y = gcd * nextPrime((math.ceil(xb/gcd))-1)

    return x, y


t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    x, y = solve(a, b,c)

    print(x, y)