def solve():
    s = input()

    n = 0

    remSet = set()

    for i in s:
        if i not in remSet:
            n+=1
            remSet.add(i)

    if n %2 != 0:
        print("IGNORE HIM!")
    

    else:
        print("CHAT WITH HER!")



solve()