n, L, a = map(int, input().split())

timeArray = []

for _ in range(n):
    t,l = map(int, input().split())

    timeArray.append((t, l))

timeArray.sort()

prev = 0

res = 0

for i in range(n):
    curr = timeArray[i][0]

    res+= ((curr-prev)//a)

    prev = curr+ timeArray[i][1]

res+= ((L- prev)//a)


print(res)

    