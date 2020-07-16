try:
    for _ in range(int(input())):
        TS = int(input())

        if TS%2 != 0:
            print(TS//2)

        else:
            ts = TS
            count = 0
            while(ts %2 == 0):
                ts/=2
                count+=1
            
            i = 2
            answer = 0
            while(i*(2**count) < TS):
                answer+=1
                i+=2
            
            print(answer)
except:
    pass

#1978243939781051