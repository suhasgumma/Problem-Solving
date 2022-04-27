import math

def solve(arr, n, k):
    med = math.ceil(n/2)

    start = (n*k)- (n-med+1)

    res = 0

    for _ in range(k):
        res+= arr[start]
        start-= (n-med+1)
    
    return res


t = int(input())


for _ in range(t):
    n , k = map(int, input().split())

    arr = list(map(int, input().split()))

    print(solve(arr, n, k))