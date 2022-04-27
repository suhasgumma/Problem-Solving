#Include - Exclude


def incExc(array, cI, prev):
    if cI == len(array):
        return 0
    
    curr = array[cI]

    include = 0

    if curr>= prev:
        include = 1+ incExc(array, cI+1, curr)
    exclude = incExc(array, cI+1, prev)

    return max(include, exclude)

print(incExc([-1,3,4,5,2,2], 0, -float('inf')))
