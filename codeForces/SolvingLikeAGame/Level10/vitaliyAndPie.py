n = int(input())

knowledge = input()

count = 0

keyHash = {}

for i in range((2*n) -2):
    if i%2 == 0:
        key = knowledge[i]

        if key in keyHash: keyHash[key]+=1

        else: keyHash[key] = 1
    
    else:
        door = knowledge[i]

        reqKey = chr(ord(door)+ 32)

        if reqKey in keyHash and keyHash[reqKey] > 0: keyHash[reqKey]-=1

        else: count+=1


print(count)



