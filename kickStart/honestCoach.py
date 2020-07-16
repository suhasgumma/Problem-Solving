no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    listt = []
    length = int(input())

    strength = input().split()
    for el in strength:
        listt.append(int(el))

    mini = abs(listt[1]- listt[0])
    for i in range(length):
        for j in range(i+1, length):
            if abs(listt[i]- listt[j]) < mini:
                mini = abs(listt[i]- listt[j])
    
    print(mini)

