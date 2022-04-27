s = input()

n = len(s)

res = ''

i = 0

while i <n-2:
    if s[i:i+3] == "WUB":
        if res != "": res+= " "

        i+= 3
    
    else:
        res+= s[i]
        i+=1

while i < n:
    res+= s[i]
    i+=1

gapCount = 0

i = len(res)-1

while i >= 0 and res[i] == " ":
    gapCount+=1
    i-=1

if gapCount == 0: print(res)

else: print(res[:-gapCount])