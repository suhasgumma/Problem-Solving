def longestWord(inp):
    start = True
    newS = ''
    maxi = 0
    maxS = ''

    for i in inp:
        if 65 <= ord(i) <= 90 or 97<= ord(i) <= 122:
            if start:
                newS = i
                start = False

            else: newS+=i
        
        else:
            if newS!= '':
                if len(newS) > maxi:
                    maxi = len(newS)
                    maxS = newS
                    newS = ''
            
            start = True
    
    if newS != '':
        if len(newS) > maxi:
            maxi = len(newS)
            maxS = newS
    
    return maxS

inp = input()

print

