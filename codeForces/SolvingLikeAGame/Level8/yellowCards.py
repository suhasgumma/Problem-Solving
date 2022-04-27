a1 = int(input())

a2 = int(input())

k1 = int(input())

k2 = int(input())

n = int(input())

remCards = n

resMax, resMin = 0, 0

if k2 < k1:
    maxPlayers = remCards//k2

    if a2 >= maxPlayers: resMax = maxPlayers

    else:
        resMax = a2

        remCards-=(k2*a2)

        maxPlayers = remCards//k1

        resMax+= (min(maxPlayers, a1))

else:
    maxPlayers = remCards//k1

    if a1 >= maxPlayers: resMax = maxPlayers

    else:
        resMax = a1

        remCards-=(k1*a1)

        maxPlayers = remCards//k2

        resMax+= (min(maxPlayers, a2))

remCards = n

threshold1 = k1-1

threshold2 = k2-1


remCards-= ((a1*threshold1) + (a2* threshold2))

resMin = max(0, remCards)


print(resMin, resMax)