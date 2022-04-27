n, k = map(int, input().split())

arr = list(map(int, input().split()))

count = k

i = 0

while i < n and count > 0:
    curr = (2*i)+1

    res = arr[curr]-1

    if res > arr[curr-1] and res > arr[curr+1]:
        arr[curr]-=1
        count-=1
    
    i+=1

print(*arr)