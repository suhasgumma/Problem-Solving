n, m = map(int, input().split())

table = []

for _ in range(n):
    row = input()
    table.append(row)


found = False

for i in range(n):
    if found: break
    for j in range(m):
        if table[i][j] == "B":
            initI = i
            initJ = j
            found = True
            break

l = 0

j = initJ

while j < m and table[initI][j] == "B":
    l+=1
    j+=1




finI, finJ = initI+ l//2+1, initJ+ l//2+1

print(finI, finJ)