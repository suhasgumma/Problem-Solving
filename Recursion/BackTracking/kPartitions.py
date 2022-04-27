def kPartition(array, K):
    arraySum = sum(array)

    if arraySum%K != 0:
        return False
    
    equalSum = arraySum//K

    bucketList = [[] for _ in range(K)]

    visited = [False for _ in range(len(array))]

    val = kPartitionHelper(array, K, equalSum, visited, equalSum, bucketList)

    if val:
        print(bucketList)
        return True
    return False


def kPartitionHelper(array, K, remSum, visited, equalSum, bucketList):
    if K ==0:
        return True
    
    for i in range(len(array)):
        el = array[i]

        if el <= remSum and not visited[i]:
            visited[i] = True
            newRemSum = remSum - el

            bucketList[K-1].append(el)

            if newRemSum == 0:
                newK= K-1
                newRemSum= equalSum
            else:
                newK = K
            
            if kPartitionHelper(array, newK, newRemSum, visited, equalSum, bucketList):
                return True
            
            visited[i] = False
            bucketList[K-1].pop()

    return False

array = list(map(int, input().split()))

print(kPartition(array, 6))

# 7 3 5 12 2 1 5 3 8 4 6 4
    