t = int(input())

for _ in range(t):
    s = input()

    l = len(s)

    n = int(s[0])

    first = (n-1)*10

    second = l* (l+1)//2


    print(first+second)
