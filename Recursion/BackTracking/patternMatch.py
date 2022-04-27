
patternDict = {}

def patternMatch(string, pattern, csI, cpI):
    if csI == len(string) and cpI == len(pattern):
        return True
    
    if csI == len(string) or cpI == len(pattern):
        return False
    
    patternChar = pattern[cpI]
    match = ''

    if patternChar not in patternDict.keys():
        for i in range(csI, len(string)):
            match+= string[i]
            patternDict[patternChar] = match

            if patternMatch(string, pattern, i+1, cpI+1):
                return True
            
            # BackTrack
            patternDict.pop(patternChar)
        return False
    
    patternString = patternDict[patternChar]

    for i in range(len(patternString)):
        index = csI+i
        if index< len(string):
            match+= (string[csI+i])
    
    if match != patternString:
        return False
    
    return patternMatch(string, pattern, csI+ len(patternString), cpI+1)

print(patternMatch('codetycode', 'XYX', 0, 0))

print(patternDict)

    