no_of_test_cases = int(input())

def pair(x,y):
    if x%2 == y%2 or abs(x-y) == 1:
        return True
    else:
        return False


for _ in range(no_of_test_cases):
    listt = []
    length = int(input())

    strength = input().split()
    for el in strength:
        listt.append(int(el))
    

    pairDict = {}
    mainFound = True
    found = False
    
    for i in range(length):
        if i in pairDict.keys():
            found = True
            continue

        found = False
        for j in range(i+1, length):
            if(pair(listt[i], listt[j])):
                if j not in pairDict.keys():
                    print(listt[i], listt[j])
                    found = True
                    pairDict[i] = listt[j]
                    pairDict[j] = listt[i]
                    break
        

        if not found:
            print('NO')
            mainFound = False
            break
    if mainFound:
        print('YES')

    print(pairDict)

        
