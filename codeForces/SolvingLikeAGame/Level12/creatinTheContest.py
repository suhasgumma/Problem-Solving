n = int(input())

arr = list(map(int, input().split()))


res = 0
j = 0

for i in range(n):
    while j < n and arr[j+1] > 2*arr[j]:
        j+=1
    
    res = max(res, j-i)

print(res)
