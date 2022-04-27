def solve(l, r):
    maxA = 2*l//3
    diff = r-l
    rem = l//3

    if rem > diff: return "Yes"
    if r <= ((2*l)-1): return "Yes"
    
    return "No"

t = int(input())


for _ in range(t):
    l, r = map(int, input().split())
    print(solve(l,r))