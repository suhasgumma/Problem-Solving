"""
Question Link:- https://www.techiedelight.com/find-binary-strings-can-formed-given-wildcard-pattern/
"""

# Use DIP DOP Method

count = 0

def binaryStringWildCard(DIP, start, end, DOP):
    global count
    if start == end:
        count+=1
        print(DOP)
        return
    
    current = DIP[start]

    if current == '?':
        DOP1 = DOP+ '1'
        DOP2 = DOP + '0'

        binaryStringWildCard(DIP, start+1, end, DOP2)
    
    else:
        DOP1 = DOP+ current
    
    binaryStringWildCard(DIP, start+1, end, DOP1)


binaryStringWildCard('1?11?00?1?', 0, 10, '')
print(count)