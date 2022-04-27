"""
The N queens puzzle is the problem of placing N chess queens on an N × N chessboard so that
no two queens threaten each other. Thus, a solution requires that no two queens share the same row,
column, or diagonal.

Question Link: https://www.techiedelight.com/print-possible-solutions-n-queens-problem/
"""

size = int(input())

board = [[False for i in range(size)] for j in range(size)]

def printBoard(board):
    for i in range(size):
        string = ''
        for j in range(size):
            if board[i][j]:
                string+= 'Q '
            else:
                string+= '_ '
        print(string)


def valid(p,q):
    for c in range(size):
        #Row check
        if board[p][c]:
            return False
        
        #Coloumn Check
        if board[c][q]:
            return False
        
    #Dio1 check
    I = p- min(p, q)
    J = q - min(p, q)

    while I < size and J< size:
        if board[I][J]:
            return False
        
        I+=1
        J+=1
    
    #Dio2 Check
    I = p - min(p, size-1-q)
    J = q + min(p, size-1-q)

    while I< size and J> 0:
        if board[I][J]:
            return False
        
        I+=1
        J-=1

        
    #If everything is Fine
    return True

def NQueens(N):
    #Base Case
    if N == 0:
        printBoard(board)
        print("**********")
        return
    
    #Check every Valid Position in the board
    for i in range(size):
        for j in range(size):
            if valid(i, j):
                board[i][j] = True
                # printBoard(board)
                NQueens(N-1)

                board[i][j] = False
    
    return -1


NQueens(10)