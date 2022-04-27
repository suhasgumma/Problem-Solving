import math

frontpage = input()

wordSet = set("Bulbasaur")


counterA = 0

counterU = 0

remCounter = {"B":0, "l": 0, "b": 0, "s": 0, "r": 0}

for let in frontpage:
    if let in wordSet:
        if let == 'a': counterA+=1

        elif let == 'u': counterU+=1

        else:
            remCounter[let]+=1


remMin = math.inf

for key in remCounter.keys():
    remMin = min(remMin, remCounter[key])


res = min(remMin, counterA//2, counterU//2)


print(res)