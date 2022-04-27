n = int(input())

arr = list(map(int,input().split()))

m = int(input())

timeStamps = []

for _ in range(m):
    s, e = map(int, input().split())

    timeStamps.append((s,e))

tot = sum(arr)

found = False

for t in timeStamps:
    s, e = t[0], t[1]

    if tot < s:
        print(s)
        found = True
        break

    if tot >= s and tot <= e:
        print(tot)
        found = True
        break

if not found:
    print(-1)


