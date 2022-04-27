"""
Modification of number of Unique paths.

Prints all the paths.
"""

maze = [
		[ 1, 1, 1, 1] ,
		[ 1, 1, 0, 1] ,
		[ 0, 1, 0, 1] ,
		[ 1, 1, 1, 1]
	]

visited = [[False for _ in range(4)] for _ in range(4)]

rowI = [0,0, 1, -1]
rowJ= [1, -1, 0, 0]

def valid(i, j):
    return 0 <= i < 4 and 0<= j<4 and not visited[i][j] and maze[i][j] == 1


paths = []

def allUniquePaths(srcI, srcJ, destI, destJ, path):
    path.append((srcI, srcJ))

    if srcI == destI and srcJ == destJ:
        newPath = path.copy()
        paths.append(newPath)
        path.pop()
        return
    
    visited[srcI][srcJ] = True

    for i in range(4):
        newI = srcI+ rowI[i]
        newJ = srcJ+ rowJ[i]

        if valid(newI, newJ):
            allUniquePaths(newI, newJ, destI, destJ, path)
        
    visited[srcI][srcJ] = False
    path.pop()
    return

allUniquePaths(0,0,3,3,[])

print(paths)
    