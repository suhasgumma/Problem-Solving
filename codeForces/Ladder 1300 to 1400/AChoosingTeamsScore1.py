n, k = map(int , input().split())

arr = list(map(int, input().split()))

count = 0

for x in arr:
    if x <= 5-k: count+=1


print(count//3)