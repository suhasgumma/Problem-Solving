row1 = list(map(int, input().split()))

row2 = list(map(int, input().split()))

row3 = list(map(int, input().split()))

sRow1 = sum(row1)
sRow2 = sum(row2)
sRow3 = sum(row3)

z = (sRow1+ sRow2- sRow3)//2

x = sRow2- z

y = sRow1 - z

row1[0] = x

row2[1] = y

row3[2] = z

print(*row1)

print(*row2)

print(*row3)