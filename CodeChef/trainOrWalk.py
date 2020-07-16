import math



try:
    no_of_test_cases = int(input())
    for _ in range(no_of_test_cases):
        N,A,B,C,D,P,Q,Y = map(int, input().split())

        cities = list(map(int,input().split()))


        B = cities[B-1]
        A = cities[A-1]
        C = cities[C-1]
        D = cities[D-1]
        
        walkTime = (B-A)*P

        withTrain = math.inf

        timeTillC = (C-A)*P


        if timeTillC <= Y:
                withTrain = Y+ ((D-C)*Q) + (abs(B-D)*P)


        print(min(walkTime, withTrain))
except:
    pass


