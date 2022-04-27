n, m = map(int, input().split())

if n == 0 and m == 0:
    print(0, 0)

elif n ==0: print("Impossible")


elif m == 0:
    print(n, n)

else:
    maxi = n+m-1

    m = max(0, m-n)

    mini = m+n

    print(mini, maxi)