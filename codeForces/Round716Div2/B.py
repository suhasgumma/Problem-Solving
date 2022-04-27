import math

def solve(n, k):
    a = int(math.pow(2, k-1)-1)

    print(a)

    res = (a* n * (n-1))+ n

    print(res)
            
    m = int((math.pow(10, 9))+ 7)

    print(m)


    return res % m


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    print(solve(n, k))
    
