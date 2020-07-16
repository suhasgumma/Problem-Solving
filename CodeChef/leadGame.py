leader = 1
max_lead = -1

score1 = 0
score2 = 0

for i in range(int(input())):
    F, S = map(int, input().split())

    score1+= F
    score2+=S

    lead = score1 - score2

    if abs(lead) > max_lead:
        if lead > 0:
            leader = 1
        else:
            leader = 2
        
        max_lead = abs(lead)


print(leader, max_lead)