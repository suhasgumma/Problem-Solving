n =int(input())

binString = input()

res = 0

curr = 0

while curr < n and binString[curr] != '0':
    res+=1
    curr+=1


if res != n: res+=1

print(res)