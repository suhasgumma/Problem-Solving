import math

def isPerfectSquare(n):
    root = math.floor(math.sqrt(n))

    if root* root == n: return True

    return False

def solve(arr, n):
    seen = set()

    for i in arr:
        if not isPerfectSquare(i): return "YES"
    
    return "NO"

t = int(input())

for _ in range(t):
    n = int(input())

    seq = list(map(int, input().split()))

    print(solve(seq, n))