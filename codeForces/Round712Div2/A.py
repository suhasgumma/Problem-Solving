def allAs(s):
    for c in s:
        if c != 'a': return False
    
    return True


def addA(s):
    n = len(s)

    for i in range(n):
        if s[n-i-1] != 'a':
            return s[:i]+ 'a'+ s[i:]


t = int(input())

for _ in range(t):
    s = input()

    if allAs(s):
        print("NO")
    
    else:
        print("YES")

        print(addA(s))

    

