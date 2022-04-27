x1, y1, x2, y2 = map(int,input().split())

if x1 == x2 and y1 == y2: print(-1)

elif y1 == y2:
    diff = abs(x1-x2)

    print(x1, y1+ diff, x2, y2+diff)

elif x1 == x2:
    diff = abs(y1-y2)
    print(x1+diff, y1, x2+diff, y2)


elif abs((y2-y1)/(x2- x1)) == 1:
    print(x1, y2, x2, y1)

else: print(-1)