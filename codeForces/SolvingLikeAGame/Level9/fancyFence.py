def solve(x):
    if 360/(180-x) == 360//(180-x):
        return "YES"
    
    return "NO"


t = int(input())

for _ in range(t):
    angle = int(input())

    print(solve(angle))