def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    hashSet = {}

    for i in arr:
        if i in hashSet: hashSet[i]+=1

        else: hashSet[i] = 1
    
    res = 0

    used = set()

    for key in hashSet.keys():

        keyUsed = key in used

        if hashSet[key] > 1 and not keyUsed:
            res+=2
            used.add(key+1)
        
        elif keyUsed:
            res+=1
            used.add(key+1)
        
        else: res+=1
    
    print(res)
    return



t = int(input())

# a,b = map(int, input().split())

# arr = list(map(int, input().split()))

for _ in range(t):
    solve()


# solve()