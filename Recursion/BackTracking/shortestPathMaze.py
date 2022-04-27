"""
Given a maze in the form of the binary rectangular matrix, find length of the shortest
path in maze from given source to given destination. The path can only be constructed out 
of cells having value 1 and at any given moment, we can only move one step in one of the four directions.
"""

matrix = [
		[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
		[0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
		[0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
		[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
		[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
		[1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
		[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
		[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
		[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
		[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
	]

visited = [[False for _ in range(10)] for _ in range(10)]
# print(visited)

def valid(i, j):
    return(0<= i< 10 and 0<= j< 10 and not visited[i][j] and matrix[i][j] == 1)

def shortestPath(srcI, srcJ, destI, destJ):
    if srcI == destI and srcJ == destJ:
        return 0
    
    visited[srcI][srcJ] = True

    rowI = [1, -1, 0, 0]
    rowJ = [0, 0, -1, 1]

    mini = float('inf')

    for i in range(4):
        newI = srcI+ rowI[i]
        newJ = srcJ+ rowJ[i]
    
        if valid(newI, newJ):
            mini = min(mini, shortestPath(newI, newJ, destI, destJ))

    visited[srcI][srcJ] = False
    return 1+ mini

print(shortestPath(0, 0, 7,5))