n = int(input())

arr = list(map(int, input().split()))

counter = [0] * 4

res = 0

for i in arr: counter[i-1]+=1

res+= counter[3]

res+= counter[2]

counter[0] = max(0, counter[0]- counter[2])


res+= (counter[1]//2)

if counter[1] %2 != 0:
    res+=1

    counter[0] = counter[0] - 2

res+= counter[0]//4

if counter[0] % 4 > 0: res+=1

print(res)