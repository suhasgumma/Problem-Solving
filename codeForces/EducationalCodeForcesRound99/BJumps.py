import math

t = int(input())

for _ in range(t):
    x = int(input())

    root = math.sqrt((1+ (8*x)))

    req = (root - 1)//2

    # print(root, req)

    curr = req* (req+1)//2

    if curr == x: print(int(req))

    else:
        req+=1

        currVal = req*(req+1)//2

        diff = currVal-x-1

        if 0 < diff <= req: print(int(req))

        else:
            print(int(req+ diff+1))
