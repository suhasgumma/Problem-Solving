def solve(str1, str2):
    n1 = len(str1)

    n2 = len(str2)

    if n1!= n2:
        return "NO"
    
    if str1 == str2: return "YES"
    
    diff1 = None
    diff2 = None


    for i in range(n1):
        if str1[i] != str2[i]:
            if diff2: return "NO"

            if diff1 == None:
                diff1 = i
            
            else: diff2 = i
    
    if diff2 == None:
        return "NO"
    
    
    if str1[diff1] == str2[diff2] and str1[diff2] == str2[diff1]: return "YES"

    return "NO"
                





str1 = input()

str2 = input()

print(solve(str1, str2))
