"""
Find total number of unique paths in a maze from source to destination.

Find the total number of unique paths which the robot can take in a given maze to reach the destination from given source.

Positions in the maze will either be open or blocked with an obstacle. The robot 
can only move to positions without obstacles i.e. solution should find paths which contain only cells
which are open. Retracing the 1 or more cells back and forth is not considered a new path. The set of 
all cells covered in a single path should be unique from other paths. At any given moment, the robot
can only move 1 step in one of 4 directions.
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


def uniquePaths(srcI, srcJ, destI, destJ):
    if srcI == destI and srcJ == destJ:
        return 1
    
    visited[srcI][srcJ] = True

    count = 0

    for i in range(4):
        newI = srcI+ rowI[i]
        newJ = srcJ+ rowJ[i]

        if valid(newI, newJ):
            count+= uniquePaths(newI,newJ,destI, destJ)
    
    visited[srcI][srcJ] = False
    
    return count


print(uniquePaths(0,0,3,3))


    