import heapq

n, m = map(int, input().split())

arr = list(map(int,input().split()))

neqArray = []

for i in arr:
    if i < 0: neqArray.append(-i)

heapq.heapify(neqArray)

nLargest = heapq.nlargest(m, neqArray)

print(sum(nLargest))
