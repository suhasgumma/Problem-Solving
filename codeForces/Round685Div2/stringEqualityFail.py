import math

def solve(sA, sB, n, k):
    if sA == sB: return "YES"

    hA, hB = {}, {}

    for s in sA:
        if s in hA: hA[s]+=1

        else: hA[s] = 1
    

    for s in sB:
        if s in hB: hB[s]+=1

        else: hB[s] = 1
    
    if hA == hB: return "YES"

    nHa, nHb = {}, {}

    for key in hA.keys():
        if key in hB:
            res = hA[key]- hB[key]
        
        else: res = hA[key]

        if key == 'z' and res > 0: return "NO"

        if res in nHa: nHa[res].add(key)

        elif res > 0:
            if res % k != 0: return "NO"

            nHa[res] = set()
            nHa[res].add(key)
    

    for key in hB.keys():
        if key in hA:
            res = hB[key]- hA[key]
        
        else: res = hB[key]

        if key == 'a' and res > 0: return "NO"

        if res in nHb: nHb[res].add(key)

        elif res > 0:
            if res % k != 0: return "NO"
            
            nHb[res] = set()
            nHb[res].add(key)
    

    # print(hA)
    # print(hB)
    # print(nHa)
    # print(nHb)
    

    sum1, sum2 = 0, 0

    for key in nHa.keys():
        sum1+= (key* len(nHa[key]))

    for key in nHb.keys():
        sum2+= (key* len(nHb[key]))
    
    # print(sum1, sum2)


    if sum1 != sum2: return "NO"

    





    return "NO"



t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    sA = input()

    sB = input()

    print(solve(sA, sB, n, k))    
    

