def solve(x):
    remaining = x
    res = 0

    currentNiceStairs = 1

    while(remaining > 0):

        consumed = currentNiceStairs *(currentNiceStairs+1)//2

        remaining -= consumed

        if remaining < 0:
            return res
        
        res+=1

        currentNiceStairs = (2*currentNiceStairs)+1
    

    return res


t = int(input())

for _ in range(t):
    x = int(input())

    print(solve(x))