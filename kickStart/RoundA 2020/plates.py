t = int(input())

def rec(plates, currIndeces, n, k, p, taken):

    if taken == p: return 0

    ans = 0

    for i in range(n):
        if currIndeces[i] < k:
            newindeces = currIndeces.copy()

            newindeces[i]+=1

            currRes = plates[i][newindeces[i]-1]+ rec(plates, newindeces, n, k, p, taken+1)

            ans = max(ans, currRes)
    
    return ans



for i in range(t):
    n, k, p = map(int, input().split())

    plates = []

    for _ in range(n):
        plate = list(map(int, input().split()))

        plates.append(plate)

    currIndeces = [0 for _ in range(n)]

    res = (rec(plates, currIndeces, n, k, p, 0))

    print("Case #"+ str(i+1)+ ": " + str(res))

