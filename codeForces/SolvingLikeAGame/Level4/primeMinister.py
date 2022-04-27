n = int(input())

seats = list(map(int, input().split()))

totalSeats = sum(seats)

if seats[0] > totalSeats//2:
    print(1)
    print(1)

else:
    res = [1]

    coalitionEligibility = seats[0]//2

    currSeats = seats[0]

    i = 1

    while currSeats <= totalSeats//2 and i <n:

        if seats[i] <= coalitionEligibility:
            res.append(i+1)
            currSeats+= seats[i]
        
        i+=1

    if currSeats<= totalSeats//2: print(0)

    else:
        print(len(res))

        print(*res)
