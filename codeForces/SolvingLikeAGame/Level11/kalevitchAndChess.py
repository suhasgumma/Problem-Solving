def isRowSlash(matrix, r):
    row = ''

    for i in range(8):
        row+= matrix[r][i]
    
    goal = 'B' * 8

    return row == goal


def isColSlash(matrix, c):
    col = ''

    for i in range(8):
        col+= matrix[i][c]
    
    goal = 'B' * 8

    return col == goal


matrix = []

for _ in range(8):
    row = input()

    matrix.append(row)

res = 0

i = 0
j = 0

while i < 8 and j < 8:
    curr = matrix[i][j]

    if curr == 'B':
        if j == 0:
            if isRowSlash(matrix, i): res+=1

        if i == 0:
            if isColSlash(matrix, j): res+=1
    
    if j ==7:
        j = 0
        i+=1
    
    else: j+=1


if res == 16:
    print(8)


else:
    print(res)
