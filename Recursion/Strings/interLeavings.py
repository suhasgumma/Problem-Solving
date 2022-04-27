"""
Question Link:- https://www.techiedelight.com/find-interleavings-of-given-strings/
"""
DOPdict = {}
def interLeavings(string1, string2, start1, start2, DOP):
    if start1 == len(string1):
        while(start2 < len(string2)):
            DOP+= string2[start2]
            start2+=1
        
        if DOP not in DOPdict.keys():
            print(DOP)
            DOPdict[DOP] = True
        return
    if start2 == len(string2):
        while(start1 < len(string1)):
            DOP+= string1[start1]
            start1+=1
        if DOP not in DOPdict.keys():
            print(DOP)
            DOPdict[DOP] = True
        return
    
    DOP1 = DOP+string1[start1]
    DOP2 = DOP+ string2[start2]

    interLeavings(string1, string2, start1+1, start2, DOP1)
    interLeavings(string1, string2, start1, start2+1, DOP2)


interLeavings('ABC', 'ACB', 0, 0, '')
