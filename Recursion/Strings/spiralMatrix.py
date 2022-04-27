matrix = [
		[1,  2,  3,  4,  5],
		[16, 17, 18, 19, 6],
		[15, 24, 25, 20, 7],
		[14, 23, 22, 21, 8],
		[13, 12, 11, 10, 9]
	]


visited = [[False for _ in range(5)] for _ in range(5)]

def spiralMatrix(I, J):
    visited[I][J] = True
    print(matrix[I][J])

    rowI= [0, 1, 0, -1]
    rowJ = [1, 0, -1, 0]

    for i in range(4):
        newI = I+ rowI[i]
        newJ = J+ rowJ[i]

        if 0<= newI < 5 and 0<= newJ < 5 and not visited[newI][newJ]:
            spiralMatrix(newI, newJ)
    
    return

spiralMatrix(0,0)
