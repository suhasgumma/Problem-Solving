N = int(input())

strList = []
for _ in range(N):
    s = input()
    sSet = set()

    for i in s: sSet.add(i)

    strList.append(sSet)

visited = set()

res = 0

for i in range(N):
    count = 1
    if i in visited: continue
    visited.add(i)
    for j in range(i+1, N):
        if strList[i] == strList[j]: count+=1
    
    res+= (count//2)

print(res)


