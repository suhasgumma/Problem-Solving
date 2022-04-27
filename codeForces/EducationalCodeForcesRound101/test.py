def whoIsFirst(tup1, tup2):
	for i in range(3):
		if tup1[i] < tup2[i]:
			return 1
		
		if tup1[i] > tup2[i]:
			return 2
	
	return 1


def insertIntoResArray(a, b, c, resArray):
	arr = sorted([a, b, c])
	
	print(arr)
	
# 	tup = (arr[0], arr[1], arr[2])
	
	resArray.append(arr)
	
	curr = len(resArray)-1, print(resArray)
	
	while curr > 0:
		prev = curr-1
		
		prevTuple = resArray[prev]
		currTuple = resArray[curr]
		
		if whoIsFirst(prevTuple, currTuple) == 1: break
			
		resArray[prev], resArray[curr] = curr, prev
		
		curr-=1
	


def threeNumberSum(array, targetSum):
    # Write your code here.
    resArray = []
    n = len(array)
    for i in range(n-2):
        compSet = set()
        a = array[i]
        newTs = targetSum - a
        for j in range(i+1, n):
            b = array[j]
            
            if b in compSet:
                c = newTs - b
                insertIntoResArray(a, b, c, resArray)
            else:
                compSet.add(newTs- b)
                
    return resArray


array = [12,3,1,2,-6, 5, -8,6]
tS = 0
print(threeNumberSum(array, tS))
