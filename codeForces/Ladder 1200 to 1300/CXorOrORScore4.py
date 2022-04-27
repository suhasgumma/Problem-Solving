def solve(a, b):
    if len(a) != len(b): return "NO"

    n = len(a)

    if n == 1:
        if a == b: return "YES"

        else: return "NO"

    i = n-1

    ai = a[i]

    if ai != b[i]:
        left = a[i-1]

        if ai == "0" and left != "1": return "NO"

        else:
            if left != "1": return "NO"
    
    i-=1

    while i > 0:
        ai = a[i]
        left = a[i-1]
        right = a[i+1]

        if ai != b[i]:

            if ai == "0":
                if left!= "1" and right != "1": return "NO"
            else:
                if right != "1": return "NO"
        
    
    right = a[i+1]

    if a[i]!= b[i]:
        if right != "1": return "NO"
    

    return "YES"


a = input()
b = input()

print(solve(a, b))
