t = int(input())

for _ in range(t):
    n, c0, c1, h = map(int, input().split())

    s = input()
    
    zeroCount, oneCount = 0, 0

    for i in s:
        if i == '0': zeroCount+=1

        else: oneCount+=1
    
    save = abs(c0-c1)

    if save > h:
        if c0 < c1:
            res = (n* c0) + (oneCount*h)
        
        else:
            res = (n*c1)+ (zeroCount*h)
    
    else:
        res = (zeroCount*c0)+ (oneCount* c1)
    

    print(res)