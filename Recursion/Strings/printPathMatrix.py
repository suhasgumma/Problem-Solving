
visited = [[False for _ in range(3)] for _ in range(3)]
matrix = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
def printPath(I, J, path):

    path.append(matrix[I][J])
    if I == 2 and J == 2:
        print(path)
        path.pop()
        return
    
    visited[I][J] = True

    #Down
    downI = I+1
    downJ = J

    if 0<= downI < 3:
        printPath(downI, downJ, path)
    
    #Right

    rightJ = J+1

    if 0<= rightJ <3:
        printPath(I, rightJ, path)
    
    path.pop()

    return

printPath(0,0,[])
