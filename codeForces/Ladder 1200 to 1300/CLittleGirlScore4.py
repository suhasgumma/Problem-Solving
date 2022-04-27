def solve(n, arr, quiries):
    arr = sorted(arr)

    count = [0]*n

    for q in quiries:
        s = q[0]-1
        e = q[1]

        for i in range(s, e): count[i]+=1
    
    count = sorted(count)

    res = 0

    for i in range(n):
        res+= (count[i]* arr[i])
    

    return res



n, q = map(int, input().split())

arr = list(map(int, input().split()))

quiries = []

for _ in range(q):
    s, e = map(int, input().split())

    quiries.append((s,e))

print(solve(n, arr, quiries))