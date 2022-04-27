import math

n  = int(input())


if n%2 != 0: print(0)

else:
    print(int(math.pow(2, n//2)))