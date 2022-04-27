def subsetMex(arr):
    hashSet = {}
 
    for i in arr:
        if i in hashSet: hashSet[i]+=1
        else: hashSet[i] = 1
 
    mex = None
 
    for i in range(102):
        if i not in hashSet:
            mex = i
            break
    
    for i in range(mex):
        if hashSet[i] < 2: return mex+i
    
 
    return 2*mex
 
 
t = int(input())
 
for _ in range(t):
    n = int(input())
 
    arr = list(map(int, input().split()))
 
    print(subsetMex(arr))