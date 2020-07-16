try:
    no_of_test_cases = int(input())
    for _ in range(no_of_test_cases):
        
        string = input()

        pair = 0

        i = 0

        # print(string, pair, i)

        # print(i)
        while(i< (len(string)-1)):
            if string[i] != string[i+1]:
                # print(type(string[i]), string[i+1])
                pair+=1
                i+=2
            else:
                i+=1
        print(pair)
    
except:
    pass

