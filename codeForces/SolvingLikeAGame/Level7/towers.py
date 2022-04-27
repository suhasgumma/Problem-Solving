n = int(input())

bars = list(map(int, input().split()))

barCounter = {}

for b in bars:
    if b in barCounter: barCounter[b]+=1

    else: barCounter[b] = 1

total = len(barCounter)

maxH = 0

for key in barCounter.keys():
    maxH = max(maxH, barCounter[key])


print(maxH, total)