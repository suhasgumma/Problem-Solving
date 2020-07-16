import math

def BinaryToDecimal(n):  
    binary = n
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    
    return decimal

def decimalToBinary(n):
    q = bin(n)
    an = ''
    for i in range(2,len(q)):
        an += q[i]
    return an


no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    n, m = input().split()
    n = int(n)
    m = int(m)

    n_dict = {}

    for i in range(n):
        n_dict[input()] = True

    middle = m/2

    left = 0
    right = 0

    for rem in n_dict.keys():
        if BinaryToDecimal(rem) < middle:
            left+=1
        else:
            right+=1
    
    displaced = abs(left- right)


    if left > right:
        correctSpot = int(math.ceil(middle+ displaced))

        while decimalToBinary(correctSpot) not in n_dict:
            correctSpot+=1
        
    if right > left:
        correctSpot = int(math.floor(middle+ displaced))
        while decimalToBinary(correctSpot) not in n_dict:
            correctSpot-=1

    
    print(decimalToBinary(correctSpot))

    