"""
Given a rectangular path in the form of binary matrix, find the length of longest possible 
route from source to destination position of the matrix by moving to only non-zero adjacent 
positions i.e. route can be formed from positions having their value as 1.
Note there should not be any cycles in the output path.

Question Link: https://www.techiedelight.com/find-longest-possible-route-matrix/
"""

size = int(input("Enter the size of the matrix: "))

"""
Input:
size = 10

matrix:

1 0 1 1 1 1 0 1 1 1
1 0 1 0 1 1 1 0 1 1
1 1 1 0 1 1 0 1 0 1
0 0 0 0 1 0 0 1 0 0
1 0 0 0 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 0
1 0 0 0 1 0 0 1 0 1
1 0 1 1 1 1 0 0 1 1
1 1 0 0 1 0 0 0 0 1
1 0 1 1 1 1 0 1 0 0 

For the inputs (0,0, 5,7) answer = 22
"""

#Enter all the rows in spaces

matrix = []

for _ in range(size):
    row = list(input().split())
    matrix.append(row)


def valid(i, j):
    if 0<= i <size and 0<= j< size:
        return True
    return False

visited = [[False for _ in range(size)] for _ in range(size)]

def longestPossibleRoute(srcI, srcJ, destI, destJ):
    # print("Hoiii")
    if srcI== destI and srcJ == destJ:
        # print(srcI,srcJ)
        return 0
    
    visited[srcI][srcJ] = True

    rowI = [-1, 1, 0, 0]
    rowJ = [0, 0, -1, 1]

    maxi = -1

    for i in range(4):
        newI= srcI+ rowI[i]
        newJ = srcJ+ rowJ[i]


        if valid(newI, newJ) and not visited[newI][newJ]:
            if matrix[newI][newJ] == '1':
                print(newI, newJ)
                val = longestPossibleRoute(newI, newJ, destI, destJ)
                print(val)
                maxi = max(maxi, val)

    
    visited[srcI][srcJ] = False

    if maxi == -1:
        return -1

    return 1+ maxi

print(longestPossibleRoute(0,0,5,7))
