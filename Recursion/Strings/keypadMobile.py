keypad = [
		[],
		[],
		['A', 'B', 'C'],
		['D', 'E', 'F'],
		['G', 'H', 'I'],
		['J', 'K', 'L'],
		['M', 'N', 'O'],
		['P', 'Q', 'R', 'S'],
		['T', 'U', 'V'],
		['W', 'X', 'Y', 'Z']
	]

c = 0
def mobileCombinations(DIP, start, DOP):
    global c
    if start == len(DIP):
        c+=1
        print(DOP)
        return
    
    current = keypad[DIP[start]]

    for i in range(len(current)):
        DOP1 = DOP+ current[i]
        mobileCombinations(DIP, start+1, DOP1)


mobileCombinations([2,3,4], 0, '')

print(c)