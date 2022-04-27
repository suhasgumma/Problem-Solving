def buildForwardMatrix(mat, n, m):

    fMatrix = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            curr = mat[i][j]

            if i == 0 and j == 0:
                if curr == 1: fMatrix[0][0] = 1
                continue
            

            if curr == -1:
                fMatrix[i][j] = -1
                continue
            
            up, left = -1, -1

            if i == 0: up = fMatrix[i][j-1]

            elif j == 0: left = fMatrix[i-1][j]

            else:
                up = fMatrix[i][j-1]
                left = fMatrix[i-1][j]
            
            maxUntilNow = max(up, left)

            if maxUntilNow == -1:
                fMatrix[i][j] = -1
                continue

            if curr == 1:
                fMatrix[i][j] = maxUntilNow+1
            
            else: fMatrix[i][j] = maxUntilNow
    

    return fMatrix



def reShapeMatrix(mat, fMatrix, n, m):
    i, j = n-1, m-1

    while i >=0 and j >=0:
        curr = fMatrix[i][j]

        if i == 0 and j == 0:
            if mat[0][0] == 1: mat[0][0] = 0

            break

        up, left = -1, -1

        if i > 0: up = fMatrix[i-1][j]

        if j > 0: left = fMatrix[i][j-1]

        if up > left:
            if mat[i-1][j] == 1: mat[i-1][j] = 0

            i-=1
        
        else:
            if j > 0:
                if mat[i][j-1] == 1: mat[i][j-1] = 0
                j-=1
        
        


    return mat


def backWardsMatrix(mat, n, m):
    fMatrix = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            curr = mat[i][j]

            if i == n-1 and j == m-1:
                continue
            

            if curr == -1:
                fMatrix[i][j] = -1
                continue
            
            down, rght = -1, -1

            if i == n-1: right = fMatrix[i][j+1]

            elif j == m-1: down = fMatrix[i+1][j]


            else:
                down = fMatrix[i][j+1]
                right = fMatrix[i+1][j]
            
            maxUntilNow = max(down, right)

            if maxUntilNow == -1:
                fMatrix[i][j] = -1
                continue

            if curr == 1:
                fMatrix[i][j] = maxUntilNow+1
            
            else: fMatrix[i][j] = maxUntilNow
    

    return fMatrix



def collectMax(mat, n, m):

    if mat[0][0] == -1 or mat[n-1][m-1] == -1:
        return 0

    frwdMatrix = buildForwardMatrix(mat, n, m)

    newMat = reShapeMatrix(mat, frwdMatrix,n, m)

    # print(newMat)

    bMatrix = backWardsMatrix(newMat, n, m)

    # print(bMatrix)

    res = frwdMatrix[n-1][m-1] + bMatrix[0][0]

    return res


mat = [[0, 1, -1], [1, 0, -1], [1, 1,1]]
mat2 = [[0, 1,1], [1, 0, -1], [1, 1,-1]]

print(collectMax(mat2, 3, 3))