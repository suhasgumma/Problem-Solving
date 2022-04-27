def rev(string):
    res = ''

    n = len(string)

    for i in range(n): res+= (string[n-i-1])

    return res

string = input()

print(string+ rev(string))
