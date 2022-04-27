import copy
def symmetric(matrix):
    return matrix[0][1]== matrix[1][0] and matrix[0][0] == matrix[1][1]

def reflexive(matrix1, matrix2):
    if matrix1[0][0] == matrix2[0][0] and matrix1[1][1] == matrix2[1][1]:
        return matrix1[0][1] == matrix2[1][0] and matrix1[1][0] == matrix2[0][1]
    
    return False
        


def solve(n, m):

    found = False
    for _ in range(n):
        row1 = list(map(int,input().split()))
        row2 = list(map(int,input().split()))

        # print(row1,row2)

        if row1[1] == row2[0]: found = True
    


    if m%2 != 0: return "NO"

    if found: return "YES"
    

    return "NO"



t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    print(solve(n,m))


