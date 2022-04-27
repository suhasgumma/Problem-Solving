n, m = map(int, input().split())

arr = list(map(int, input().split()))

counterArr = [0 for _ in range(n)]

for i in arr:
    counterArr[i-1]+=1

print(min(counterArr))