# def solve(n):
#     if n == 1: return 0
#     get_bin = lambda x: format(x, 'b')

#     k = get_bin(n)

#     k  =len(k)-1

#     resS = '1'* k

#     return int(resS, 2)



# t = int(input())

# for _ in range(t):
#     n = int(input())

#     print(solve(n))


# string = "pty"

# print(string[:-1])

def phoneNumberMnemonics(phoneNumber):
    poss = {"1": "1", "2": "2abc", "3": "3def", "4": "4ghi", "5": "5jkl", "6": "6mno", "7": "7pqrst", "8":"8uvw", "9": "9wxyz", "0": "0"}
	
	
    return helper(phoneNumber, poss)


def helper(phnNo, possibilities):
	if phnNo == "": return [""]
	
	prev = helper(phnNo[:-1], possibilities)
	
	curr = phnNo[-1]
	res = []
	
	for poss in possibilities[curr]:
		for currnt in prev:
			res.append(currnt+ poss)
		
	
	return res
print(phoneNumberMnemonics("1905"))