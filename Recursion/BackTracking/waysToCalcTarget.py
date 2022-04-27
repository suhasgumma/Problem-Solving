array = list(map(int, input().split()))
target = int(input())

def totalWaysToTarget(array, size, remSum):
    if remSum == 0:
        return 1
    
    if size == 0:
        return 0
    
    el = array[size-1]
    
    decisions = [1, -1, 0]

    count = 0

    for i in range(3):
        newRem = remSum + (decisions[i]*el)
        count += totalWaysToTarget(array, size-1, newRem)
    
    return count

print(totalWaysToTarget(array, len(array), target))

