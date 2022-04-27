def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    diffs = set()

    res = 0

    for i in range(n):
        for j in range(i+1, n):
            diff = arr[j] - arr[i]

            if diff not in diffs:
                res+=1
                diffs.add(diff)
    
    print(res)
    return



t = int(input())

# a,b = map(int, input().split())

# arr = list(map(int, input().split()))

for _ in range(t):
    solve()


# solve()