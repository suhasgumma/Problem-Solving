no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    n, m = input().split()
    n = int(n)
    m = int(m)

    n_dict = {}

    for i in range(n):
        n_dict[input()] = True
    
    finalSize = 2**m

    listt = ['0','1']

    while len(listt) != finalSize:
        r = listt.pop(0)
        r1 = r+'0'
        r2 = r+'1'

        listt.append(r1)
        listt.append(r2)
    
    new_list = []

    for el in listt:
        if el not in n_dict.keys():
            new_list.append(el)
    

    new_length = len(new_list)
    
    print(new_list[int((new_length-1)/2)])
