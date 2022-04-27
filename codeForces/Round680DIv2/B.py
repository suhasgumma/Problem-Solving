
t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))

    res1 = arr[0]+ arr[1]

    res2 = arr[2]+ arr[3]

    print(max(res1, res2))