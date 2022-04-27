n = int(input())

arr = list(map(int, input().split()))

maxim = max(arr)

tot = sum(arr)

res = (2*maxim) - tot+1

print(res)