string = input()

wordList = set()

currString = string[-1] + string[: -1]

res = 1

while currString != string:
    res+=1
    currString = currString[-1] + currString[: -1]

print(res)

