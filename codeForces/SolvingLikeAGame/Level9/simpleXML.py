xml = input()

n = len(xml)
op = 0

i = 0

memDict = {}

while i < n-3:
    poss = xml[i: i+3]

    if poss[2] == ">":
        res = (" "* op) + poss

        op+=2
        i+=3

        print(res)
    
    else:
        poss = xml[i:i+4]

        op-=2


        res = (" "* op) + poss

        


        i+=4

        print(res)
