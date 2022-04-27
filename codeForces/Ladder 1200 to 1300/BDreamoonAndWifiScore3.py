def nCr(n, r): 
  
    return (fact(n) / (fact(r)  
                * fact(n - r))) 
  
# Returns factorial of n 
def fact(n): 
  
    res = 1
      
    for i in range(2, n+1): 
        res = res * i 
          
    return res 


def solve(s, r):
    sScore, rScore = 0, 0

    unKnown = 0

    for i in s:
        if i == '+': sScore+=1

        else: sScore-=1
    
    for i in r:
        if i == '+': rScore+=1

        elif i == '-': rScore-=1

        else: unKnown+=1
    
    req = abs(rScore-sScore)

    if req > unKnown: return 0

    mR = unKnown+ req

    if mR%2 != 0: return 0

    x = mR//2

    tot = 2**unKnown

    return nCr(unKnown, x)/tot


s = input()

r = input()

print(solve(s, r))