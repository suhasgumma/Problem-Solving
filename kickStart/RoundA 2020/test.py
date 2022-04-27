#Only recursion

def reverse(arr):
	n = len(arr)
	
	i,j = 0, n-1
	
	while i < j:
		arr[i], arr[j] = arr[j], arr[i]
		i+=1
		j-=1
	
	return arr

def recHelper(str1, str2, n, m, path):
	if n == 0 or m == 0: return path
	
	if str1[n-1] == str2[m-1]:
		path.append(str1[n-1])
		return recHelper(str1, str2, n-1, m-1, path)
	
	ch1 = recHelper(str1, str2, n-1, m, path[:])
	
	ch2 = recHelper(str1, str2, n, m-1, path[:])
	
	if len(ch1) > len(ch2):
		return reverse(ch1)
	
	return reverse(ch2)

def longestCommonSubsequence(str1, str2):
	
	return recHelper(str1, str2, len(str1), len(str2), [])
    

print(longestCommonSubsequence("abdcd", "abc"))