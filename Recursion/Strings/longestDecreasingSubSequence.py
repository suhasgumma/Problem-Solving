array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

def lDSS(arrray, Index, prev):
    if Index == len(arrray):
        return 0
    
    current = arrray[Index]

    if current > prev:
        return lDSS(array, Index+1, prev)
    
    return max((1+ lDSS(array, Index+1, current), lDSS(array, Index+1, prev)))

print(lDSS(array, 0, float('inf')))

