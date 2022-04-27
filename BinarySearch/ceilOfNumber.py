def getCeilInSortedArray(array, target):
    left, right = 0, len(array)-1

    ceil = None

    while left <= right:
        mid = (left+right)//2

        if array[mid] == target: return target

        elif array[mid] > target:
            ceil = array[mid]
            right = mid-1
        
        else:
            left = mid+1
        
    
    return ceil