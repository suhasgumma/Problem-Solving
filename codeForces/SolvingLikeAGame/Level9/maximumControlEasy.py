n = int(input())

counterArray = [0] *n


for _ in range(n-1):
    s, g = map(int, input().split())

    counterArray[s-1]+=1
    counterArray[g-1]+=1

res = 0

for i in counterArray:
    if i ==1: res+=1


print(res)

