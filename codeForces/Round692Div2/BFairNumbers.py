def isFair(num):
    s = str(num)
    n  =len(s)

    for idx in range(n):
        curr = int(s[idx])

        if curr == 0: continue

        if num% curr!= 0: return False
    
    return True


def solve(s):
    num = int(s)
    
    while not isFair(num): num+=1

    return num


t = int(input())

for _ in range(t):
    print(solve(input()))