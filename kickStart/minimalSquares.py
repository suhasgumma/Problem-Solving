no_of_test_cases = int(input())

for i in range(no_of_test_cases):
    a, b = input().split()
    a = int(a)
    b = int(b)

    mini =  min(a,b)
    maxi = max(a,b)

    if 2*mini >= maxi:
        print(2*mini*2*mini)
    else:
        print(maxi*maxi)

    