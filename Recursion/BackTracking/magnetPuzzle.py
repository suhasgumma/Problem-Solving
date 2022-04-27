top = [1, -1, -1, 2, 1, -1]
bottom = [2, -1, -1, 2, -1, 3]
left = [2, 3, -1, -1, -1]
right = [-1, -1, -1, 1, -1]

rules = [
		['L', 'R', 'L', 'R', 'T', 'T'],
		['L', 'R', 'L', 'R', 'B', 'B'],
		['T', 'T', 'T', 'T', 'L', 'R'],
		['B', 'B', 'B', 'B', 'T', 'T'],
		['L', 'R', 'L', 'R', 'B', 'B']
    ]


M, N = 5, 6

board = [['_' for _ in range(N)] for _ in range(M)]

topC = [0 for _ in range(N)]
bottomC = [0 for _ in range(N)]
leftC = [0 for _ in range(M)]
rightC = [0 for _ in range(M)]

def printBoard(board):
    for i in range(M):
        string = ''
        for j in range(N):
            string+= board[i][j]
        print(string)

#Task1 Get Blocks From the Rules
visited = [[False for _ in range(N)] for _ in range(M)]

def getBlocks(rules):
    blocks = []
    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                rule = rules[i][j]
                i1 = (i, j)
                if rule == 'R' or rule == 'L':
                    i2 = (i, j+1)
                else:
                    i2 = (i+1, j)
                visited[i][j] = True
                visited[i2[0]][i2[1]] = True
                blocks.append((i1,i2))
    return blocks

blocks= getBlocks(rules)


#Task2 Check If board follows the constraints.
def followingConstraints(board):
    for i in range(N):
        if top[i]!= -1 and top[i] != topC[i]:
            return False
        
        if bottom[i]!= -1 and bottom[i] != bottomC[i]:
            return False
    
    for i in range(M):
        if left[i]!= -1 and left[i] != leftC[i]:
            return False
        
        if right[i]!= -1 and right[i] != rightC[i]:
            return False
    
    return True

#Task 3 Check If It is legal To place A sign in the current Cell
def legal(i, j, sign):
    rowI = [0,0,1,-1]
    rowJ = [1, -1,0, 0]
    for c in range(4):
        I = i+ rowI[c]
        J = j+ rowJ[c]

        if 0<= I < M and 0<= J< N:
            if board[I][J] == sign:
                return False
    
    return True


#Final Task Write the recursive backTracking

def magnetPuzzle(block):
    if block == (N*M)//2:
        if followingConstraints(board):
            printBoard(board)
            return True
        return False
    
    #Get the posns of the current block
    blockIndeces = blocks[block]

    firstI = blockIndeces[0][0]
    firstJ = blockIndeces[0][1]

    secondI = blockIndeces[1][0]
    secondJ = blockIndeces[1][1]

    #Possibility 1 (+, -)
    if legal(firstI, firstJ, '+') and legal(secondI, secondJ, '-'):
        board[firstI][firstJ] = '+'
        board[secondI][secondJ] = '-'
        topC[firstJ] +=1
        bottomC[secondJ] +=1
        leftC[firstI]+=1
        rightC[secondI]+=1

        if magnetPuzzle(block+1):
            return True
        
        #BackTrack
        board[firstI][firstJ] = '_'
        board[secondI][secondJ] = '_'
        topC[firstJ] -=1
        bottomC[secondJ] -=1
        leftC[firstI]-=1
        rightC[secondI]-=1

    #Possibility 2 (-, +)
    if legal(firstI, firstJ, '-') and legal(secondI, secondJ, '+'):
        board[firstI][firstJ] = '-'
        board[secondI][secondJ] = '+'
        topC[secondJ] +=1
        bottomC[firstJ] +=1
        leftC[secondI]+=1
        rightC[firstI]+=1

        if magnetPuzzle(block+1):
            return True
        
        #BackTrack
        board[firstI][firstJ] = '_'
        board[secondI][secondJ] = '_'
        topC[secondJ] -=1
        bottomC[firstJ] -=1
        leftC[secondI]-=1
        rightC[firstI]-=1
    

    #Possibility 3 (X X)
    board[firstI][firstJ] = "X"
    board[secondI][secondJ] = 'X'

    if magnetPuzzle(block+1):
        return True
        
    #BackTrack
    board[firstI][firstJ] = '_'
    board[secondI][secondJ] = '_'


    return False

magnetPuzzle(0)


    
    
                    
                    



