def biggerIsGreater(string):
    l = len(string)

    for i in range(l-1, 0, -1):
        for j in range(i-1, -1, -1):
            if string[i] > string[j]:
                part1 = string[0:j]
                part2 = string[j+1:i]
                part3 = string[i+1:]

                res = part1+ string[i]+ part2+ string[j]+ part3

                res1 = res[:j+1]
                res2 = sorted(res[j+1: ])

                res = res1

                for s in res2: res+= s


                return res
    
    return 'no answer'


for i in range(100):
    t = input()

    print(biggerIsGreater(t))
