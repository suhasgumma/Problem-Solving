"""
Generate list of possible words from a character matrix.
Given a M x N boggle board, find list of all possible words that can be formed
by a sequence of adjacent characters on the the board.

We are allowed to search a word in all eight possible directions
i.e. North, West, South, East, North-East, North-West, South-East, 
South-West, but a word should not have multiple instances of the same cell.

Question Link: https://www.techiedelight.com/generate-list-of-possible-words-from-a-character-matrix/
"""

board = [
		['M', 'S', 'E'],
		['R', 'A', 'T'],
		['L', 'O', 'N']
	]


words = ["STAR", "NOTE", "SAND", "STONE"]

visited = [[False for _ in range(3)] for _ in range(3)]

wordList = []

def valid(i, j):
    return (0<= i< 3 and 0<= j< 3 and not visited[i][j])


def allPossibleWords(I, J, string):
    newString = string + board[I][J]

    if newString in words:
        # print(I, J)
        wordList.append(newString)
        return
    
    visited[I][J] = True
    

    rowI = [1, -1, 0, 0, 1 ,-1, 1, -1]
    rowJ = [0, 0, 1, -1, 1, -1, -1, 1]

    for c in range(8):
        newI = I+ rowI[c]
        newJ = J+ rowJ[c]

        # print(newI, newJ)

        if valid(newI, newJ):
            allPossibleWords(newI, newJ, newString)
    
    visited[I][J] = False

    return

for i in range(3):
    for j in range(3):
        allPossibleWords(i, j, "")

print(wordList)
