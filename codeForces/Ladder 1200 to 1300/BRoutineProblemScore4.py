import math

def solve(a, b, c, d):
    if a == c and c == d: return "0/1"

    if a <c or b <d:
        x1 = c/a
        x2 = d/b

        if x1 > x2:
            num = int((b*c) - (d*a))
            den = c*b
        
        else:
            num = int((a*d) - (b*c))
            den = d*a
        
        # up = math.ceil(math.sqrt(num))

        # print(num, den, up)

        i = 2
        while i <= num:
            if num%i == 0 and den%i == 0:
                num = num//i
                den = den//i
                # print(num, den, i)
            else: i+=1
            
        
        if num == 0: den = 1
        
        
        return str(num) + "/" + str(den)
    
    x1 = a/c

    x2 = b/d

    if x2 < x1:
        if int(x2) == x2 or int(c*x2) == c*x2:
            num = int(a - (x2*c))
            den =a
        else:
            num = (a*d) - (c*b)
            den = a*d
    

    else:
        if int(x1) == x1 or int(x1*d) == x1*d:
            num = int(b -(x1*d))
            den = b
        
        else:
            num = (c*b) - (a*d)
            den = c*b
    

    # print(num, den)
    up = math.ceil(math.sqrt(num))

    # print(num, den, up)

    i = 2
    while i <= num:
        if num%i == 0 and den%i == 0:
            num = num//i
            den = den//i
            # print(num, den, i)
        else: i+=1
    
    if num == 0: den = 1

    

    return str(num)+ "/"+ str(den)    

a,b,c,d = map(int, input().split())

print(solve(a,b, c, d))
