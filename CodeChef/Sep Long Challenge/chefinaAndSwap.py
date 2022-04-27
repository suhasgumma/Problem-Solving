import math
def niceSwaps(N):
    summ = N*(N+1)/2

    swaps = 0

    if summ%2 != 0: return 0


    #without swaps
    root = math.sqrt(1+ (4*summ))
    M = (root-1)/2


    if M.is_integer() and 1<= M< N:
        swaps+= M*(M-1)//2
        swaps+= (N-M)*(N-M-1)//2
    
    #with swaps
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            swapGainDoub = (j-i)*2
            root = math.sqrt(1+ (4*(summ-swapGainDoub)))
            M = (root-1)/2

            if M.is_integer() and i<= M< j:
                # print(i,j,M)
                swaps+=1
    
    # print("****************")
    
    return swaps

def niceSwapsOptimal(N):
    if N == 3: return 2

    summ = N*(N+1)/2

    swaps = 0

    if summ%2 != 0: return 0

    #without swaps
    root = math.sqrt(1+ (4*summ))
    M = (root-1)/2


    if M.is_integer() and 1<= M< N:
        swaps+= M*(M-1)//2
        swaps+= (N-M)*(N-M-1)//2

    
    #with Swaps
    swapAcross = int(math.ceil(N/4) + 1)

    swaps+= swapAcross

    return swaps


def niceSwapsOptimal2(N):
    if N == 3: return 2

    summ = N*(N+1)/2

    swaps = 0

    if summ%2 != 0: return 0


    #without swaps
    root = math.sqrt(1+ (4*summ))
    M = (root-1)/2


    if M.is_integer() and 1<= M< N:
        swaps+= M*(M-1)//2
        swaps+= (N-M)*(N-M-1)//2
    
    for i in range(1, N):
        swapDiff = (N*(N+1)/4) - (i*(i+1)/2)

        

        if swapDiff.is_integer() and 0 < swapDiff < N:
            # print(swapDiff, i)
            right = min(N, i+swapDiff)
            left = max(1, i-swapDiff+1)
            space = right-left+1
            swaps+= (space-swapDiff)
    
    return int(swaps)


def niceSwapsOptimal3(N):
    if N == 0: return 0
    summ = N*(N+1)//2

    if summ%2 != 0: return 0

    M = math.sqrt(1+(4*summ))

    M = (M-1)/2

    swaps = 0

    if M.is_integer() and 1<= M< N:
        swaps+= M*(M-1)//2
        swaps+= (N-M)*(N-M-1)//2
        swaps-=1

    M = math.ceil(M)

    swaps+= (N-M+1)

    return swaps


N = int(input())

for i in range(N):
    s1 = niceSwaps(i)
    s2 = niceSwapsOptimal3(i)


    if s1!= s2:
        print(i, s1, s2)
    


