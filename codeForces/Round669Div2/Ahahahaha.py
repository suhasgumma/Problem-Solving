def balanceArray(arr):
    l = len(arr)

    noZeroes = 0

    for i in arr:
        if i == 0: noZeroes+=1
    
    noOnes = l- noZeroes

    if noOnes <= (l/2):
        return [0]*noZeroes

    else:
        if noOnes%2 == 0:
            return [1]*noOnes
        
        else:
            return[1]*(noOnes-1)
        

        


            


T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    res = balanceArray(arr)

    print(len(res))

    print(*res)



