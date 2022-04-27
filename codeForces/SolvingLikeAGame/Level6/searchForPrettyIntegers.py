n, m = map(int, input().split())

list1 = list(map(int, input().split()))

list2 = list(map(int, input().split()))

set2 = set(list2)

minCommon = 10

for i in list1:
    if i in set2:
        minCommon = min(minCommon, i)

if minCommon <10: print(minCommon)

else:
    dig1 = min(list1)
    dig2 = min(list2)

    if dig1 ==  dig2: print(dig1)

    elif dig1 < dig2:
        res = (dig1*10)+ dig2
        print(res)

    else:
        res = (dig2*10) + dig1
        print(res)