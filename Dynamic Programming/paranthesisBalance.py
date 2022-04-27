def minimum(string, cI, open, s):
    if cI == 0:
        if open == 0:
            print(s)
        return open
    
    current = string[cI-1]

    if current == ')':
        include = minimum(string, cI-1, open+1, s+ '(')
        exclude = 1+ minimum(string, cI-1, open,s)
    
    if current == '(':
        include = float('inf')
        if open != 0:
            include = minimum(string, cI-1, open-1, s+ ')')
        exclude = 1+ minimum(string, cI-1, open, s)

    # print(include, exclude)
    
    return min(include, exclude)


print(minimum('()())()', 7, 0, ''))