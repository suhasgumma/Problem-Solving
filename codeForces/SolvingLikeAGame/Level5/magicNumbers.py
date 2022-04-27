def solve(string):
    str1 = '144'
    str2 = '14'

    str3 = '1'

    n = len(string)

    i = 0

    while i < n:
        if i+2< n:
            poss =  string[i:i+3]

            if poss == str1:
                i+=3
                continue
        
        if i+1 < n:
            poss = string[i: i+2]

            if poss == str2:
                i+=2
                continue
        
        poss = string[i]

        if poss == str3:
            i+=1
            continue

        return "NO"
    

    return "YES"



string = input()

print(solve(string))