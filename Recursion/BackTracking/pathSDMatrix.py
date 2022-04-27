"""
Find path from source to destination in a matrix that satisfies given constraints.

We can move exactly k steps from any cell in the matrix where k is the
value of that cell. i.e. from any cell.

Question Link: https://www.techiedelight.com/find-path-source-destination-matrix-satisfies-given-constraints/
"""




matrix = [
		[7, 1, 3, 5, 3, 6, 1, 1, 7, 5],
		[2, 3, 6, 1, 1, 6, 6, 6, 1, 2],
		[6, 1, 7, 2, 1, 4, 7, 6, 6, 2],
		[6, 6, 7, 1, 3, 3, 5, 1, 3, 4],
		[5, 5, 6, 1, 5, 4, 6, 1, 7, 4],
		[3, 5, 5, 2, 7, 5, 3, 4, 3, 6],
		[4, 1, 4, 3, 6, 4, 5, 3, 2, 6],
		[4, 4, 1, 7, 4, 3, 3, 1, 4, 2],
		[4, 4, 5, 1, 5, 2, 3, 5, 3, 5],
		[3, 6, 3, 5, 2, 2, 6, 4, 2, 1]
	]


visited = [[False for _ in range(10)] for _ in range(10)]

def valid(i, j):
    if 0<= i < 10 and 0<= j < 10 and not visited[i][j]:
        return True
    return False

def pathSDMatrix(srcI, srcJ, destI, destJ, path):
    #Base Case
    path.append((srcI, srcJ))
    if srcI == destI and destJ == srcJ:
        print(path)
        return True
    
    visited[srcI][srcJ] = True
    # path.append((srcI, srcJ))

    current = matrix[srcI][srcJ]

    rowI = [1, -1, 0, 0]
    rowJ = [0, 0, 1,-1]

    for c in range(4):
        newI = srcI+ (rowI[c]*current)
        newJ = srcJ + (rowJ[c]* current)

        if valid(newI, newJ) and pathSDMatrix(newI, newJ, destI, destJ, path):
            return True
    
    visited[srcI][srcJ] = False
    path.pop()

    return False

pathSDMatrix(0, 0, 9, 9, [])


