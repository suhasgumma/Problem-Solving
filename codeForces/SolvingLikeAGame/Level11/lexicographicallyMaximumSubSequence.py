def solveByRec(string):

    n = len(string)
    if n == 0: return ''

    maxim = 'a'

    for c in string: maxim = max(maxim, c)

    count = 0

    for i in string:
        if i == maxim: count+=1

    
    # print(maxim)
    
    for i in range(n-1, -1, -1):
        if string[i] == maxim:
            lastAppearence = i+1
            break
    
    firstPart = maxim* count

    secondPart = solveByRec(string[lastAppearence:])

    return firstPart+ secondPart


string = input()

print(solveByRec(string))    