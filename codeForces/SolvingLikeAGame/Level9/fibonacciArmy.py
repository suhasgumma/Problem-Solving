n = int(input())

prev2 = 1
prev1 = 1

res = 0

if n == 1: print(1)

else:
    for i in range(2, n+1):
        res = prev1+ prev2

        prev2 = prev1
        prev1 = res
    

    print(res)