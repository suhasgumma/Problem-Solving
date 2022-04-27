n = int(input())

binString = input()

oneCount = 0

zeroCount = 0

for bit in binString:
    if bit == '1': oneCount+=1
    else: zeroCount+=1

res = ''

if oneCount>0:
    res+= '1'

    for _ in range(zeroCount): res+= '0'

    print(res)

else: print('0')