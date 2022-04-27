"""
Given a chess board, print all sequences of moves of a knight on a chessboard such
that the knight visits every square only once.

Question Link: https://www.techiedelight.com/print-possible-knights-tours-chessboard/
"""

size = int(input())

visited = [[-1 for i in range(size)] for j in range(size)]


def printBoard(visited):
    for i in range(size):
        string = ''
        for j in range(size):
            string+= (str(visited[i][j]) + " ")
        
        print(string)

count = 0

def knightTour(i, j, moveCount):

    visited[i][j] = moveCount

    global count


    if moveCount == (size*size):
        printBoard(visited)
        print("******")
        visited[i][j] = -1
        count+=1
        return True
    

   

    #Move 1 Top Left 1
    if i >= 2 and j >=1:
        I = i-2
        J = j-1

        if visited[I][J] == -1:
            knightTour(I, J, moveCount+1)

    #Move 2 Top Left 2
    if i >= 1 and j >=2:
        I = i-1
        J = j-2

        if visited[I][J] == -1:
            knightTour(I, J, moveCount+1)
    
    #Move 3 Bottom Left 1
    if i < size-1 and j >=2:
        I = i+1
        J = j-2

        if visited[I][J] == -1:
            knightTour(I, J, moveCount+1)

    #Move 4 Bottom Left 2
    if i < size-2 and j >=1:
        I = i+2
        J = j-1

        if visited[I][J] == -1:
            knightTour(I, J, moveCount+1)

    #Move 5 Top Right 1
    if i >= 2 and j < size-1:
        I = i-2
        J = j+1

        if visited[I][J] == -1:
            knightTour(I, J, moveCount+1)

    #Move 6 Top Right 2
    if i >= 1 and j < size-2:
        I = i-1
        J = j+2

        if visited[I][J] == -1:
            knightTour(I, J, moveCount+1)

    #Move 7 Bottom Right 1
    if i < size-1 and j < size-2:
        I = i+1
        J = j+2

        if visited[I][J] == -1:
            knightTour(I, J, moveCount+1)

    #Move 8 Bottom Right 2
    if i < size-2 and j< size-1:
        I = i+2
        J = j+1

        if visited[I][J] == -1:
            knightTour(I, J, moveCount+1)

    visited[i][j] = -1


knightTour(0,0, 1)

print(count)