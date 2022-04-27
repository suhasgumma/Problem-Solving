def isPossible(arr, n, prev, res):
    if arr == [-1]*n: return True, []

    sumSet = {}

    # print(arr, sumSet)

    for i in range(n):
        for j in range(i+1, n):

            if arr[i] != -1 and arr[j] != -1:
                summ = arr[i]+ arr[j]

                if summ in sumSet:
                    sumSet[summ].append((i,j))
                
                else:
                    sumSet[summ] = [(i, j)]
    if prev == -1:
        for key in sumSet:
            for (i,j) in sumSet[key]:

                prevI, prevJ = arr[i], arr[j]

                arr[i], arr[j] = -1, -1

                if isPossible(arr, n, max(prevI, prevJ), res)[0]:
                    
                    res.append((prevI, prevJ))
                    res.append(key)
                    return True, res

                arr[i], arr[j] = prevI, prevJ
    
    elif prev not in sumSet: return False, []

    else:
        for (i, j) in sumSet[prev]:
            prevI, prevJ = arr[i], arr[j]

            arr[i], arr[j] = -1, -1

            if isPossible(arr, n, max(prevI, prevJ), res)[0]:
                res.append((prevI, prevJ))
                return True, []

            arr[i], arr[j] = prevI, prevJ

    
    return False, []

def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    # if not isPossible(arr, 2*n, -1):
    #     print("NO")
    #     return
    
    poss, res = isPossible(arr, 2*n, -1, [])

    if not poss:
        print("NO")
        return

    print("YES")
    
    r= len(res)
    print(res[-1])

    for i in range(r-2, -1, -1):
        i, j = res[i]

        print(i, j)

    return


t = int(input())




for _ in range(t):
    solve()