def isThere(s, zeroSet, oneSet, l, r):
    left = s[l-1]
    right = s[r-1]

    for i in range(l-1):
        if left == '0':
            if i in zeroSet: return "YES"
        
        else:
            if i in oneSet: return "YES"
    
    for i in range(r,len(s)):
        if right == '0':
            if i in zeroSet: return "YES"
        else:
            if i in oneSet: return "YES"
    
    return "NO"

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())

    s = input()

    zeroSet = set()
    oneSet = set()

    for i in range(n):
        if s[i] == '0': zeroSet.add(i)

        else: oneSet.add(i)

    for _ in range(q):
        l, r = map(int, input().split())

        print(isThere(s, zeroSet, oneSet, l, r))