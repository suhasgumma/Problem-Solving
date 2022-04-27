def solve(string, n):
    tList = []
    mList = []
  

    for i in range(n):
        if string[i] == 'T':
            tList.append(i)
        
        else: mList.append(i)
    
    if len(tList) != (2* len(mList)): return False

    lm = len(mList)
    
    for i in range(lm):
        if tList[i] > mList[i]: return False

        if tList[i+lm] < mList[i]: return False

    
    return True


t = int(input())

for _ in range(t):
    n = int(input())

    s = input()

    if solve(s, n): print("YES")

    else: print("NO")
    
