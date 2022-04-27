import math

def niceSwaps(N):
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

    return int(swaps)

try:
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        
        print(niceSwaps(N))

except:
    pass

