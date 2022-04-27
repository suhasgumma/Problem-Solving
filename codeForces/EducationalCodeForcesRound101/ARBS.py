def solve():
    s = input()

    pos1, pos2 = 0, 0

    firstQs, lastQs = -1, -1

    unAns = 0

    for i in range(len(s)):
        if s[i] == '(':
            pos1 = i
        
        elif s[i] == ')':
            pos2 = i
        
        else:
            if firstQs == -1: firstQs = i

            lastQs = i

            unAns+=1
    


    if unAns %2 != 0:
        print("NO")
        return

    if pos1 < pos2:
        print("YES")
        return
        
    
    if firstQs == lastQs:
        print("NO")
        return
    
    if firstQs < pos2 and lastQs > pos1:
        print("YES")
        return
    
    print("NO")
    return




t = int(input())

# a,b = map(int, input().split())

# arr = list(map(int, input().split()))

for _ in range(t):
    solve()