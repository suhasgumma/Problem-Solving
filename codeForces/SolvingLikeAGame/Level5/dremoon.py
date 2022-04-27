def solve(arr, n,x):

    arrSet = set(arr)

    maxi = max(arr)

    missing = []

    for i in range(1, maxi):
        if i not in arrSet:
            missing.append(i)
    

    m = len(missing)

    if m == 0: return maxi+x

    if x < m: return missing[x]-1

    return maxi+ (x-m)



t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    arr = list(map(int, input().split()))

    print(solve(arr, n, x))