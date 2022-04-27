def solve():
    a,b,k = map(int, input().split())

    res = 0

    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    degA = [0]* a

    degB = [0]* b

    for i in range(k):
        degA[l1[i]-1]+=1
        degB[l2[i]-1]+=1
    
    poss = 0

    for i in range(k):
        deg1 = degA[l1[i]-1]
        deg2 = degB[l2[i]-1]

        poss+= (k-deg1-deg2+1)
    
    print(poss//2)
    

    return


t = int(input())

for _ in range(t):
    solve()