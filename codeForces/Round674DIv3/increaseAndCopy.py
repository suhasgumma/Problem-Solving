import math

t = int(input())


for _ in range(t):
    n = int(input())

    first = math.floor(math.sqrt(n))

    second = n//first

    # print(first, second)
    rem = n - (first*second)

    if rem> 0: rem =1

    res = first+second+rem -2

    print(res)