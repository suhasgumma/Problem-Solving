def solveByRec(listt):
    if len(listt) == 0: return 0

    if len(listt) == 1:
        return 0

    lst = listt[-1]
    frst = listt[0]
    
    diff = listt[-1]- listt[0]

    l1, l2 = listt.copy(), listt.copy()

    l1.pop()
    l2.pop(0)

    diff1 = l1[-1]- l1[0]
    diff2 = l2[-1]- l2[0]

    if diff1 < diff2:
        return diff+ solveByRec(l1)
    
    elif diff2 < diff1:
        return diff+ solveByRec(l2)

    else:
        lc, rc = 0, 0

        i = 0
        initial = listt[0]

        while i < len(listt):
            if listt[i] == initial:
                lc+=1
                i+=1

            else: break
        
        j = len(listt)-1
        initial = listt[j]

        while j >= 0:
            if listt[j] == initial:
                rc+=1
                j-=1

            else: break

        
        # print(lc, rc)
        
        if lc > rc: return diff+ solveByRec(l1)

        else: return diff+ solveByRec(l1)









n = int(input())

s = list(map(int, input().split()))

s.sort()

print(solveByRec(s))
        