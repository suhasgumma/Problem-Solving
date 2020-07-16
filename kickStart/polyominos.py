def stable(block, R, C):
    for i in range(R-1):
        for j in range(C):
            if block[i][j] != 0 and block[i+1][j] == 0:
                return False
    
    return True


no_of_test_cases = int(input())

for case in range(no_of_test_cases):
    R, C = input().split()
    R = int(R)
    C = int(C)

    queue = []

    visited = {}

    listOfAllPolyominos = []

    block = [[0]*C for _ in range(R)]
    positionDict = {}

    input_block = []

    for i in range(R):
        row = input()
        input_block.append(row)
        for j in range(C):
            if row[j] not in positionDict.keys():
                positionDict[row[j]] = [(i,j)]
            else:
                positionDict[row[j]].append((i,j))

    
    for i in range(len(input_block)-1, -1, -1):
        for polyomino in input_block[i]:
            if polyomino not in visited.keys():
                queue.append(polyomino)
                visited[polyomino] = True

    visited = {}
    answer = ''

    while len(queue) !=0:
        polyomino = queue.pop(0)

        #If polynomia in visited answer = -1
        if polyomino in visited.keys():
            answer = -1
            continue
        # Add polyomomio to block if polynomio not in visited
        for pos in positionDict[polyomino]:
            block[pos[0]][pos[1]] = polyomino

        # Check if block is stable
        stablee = stable(block, R, C)
                    
        # If stable make visited Empty and append polynomia to answer
        if stablee:
            answer+=polyomino
            visited = {}
        # if not stable add polynomia to visited and remove polynomia from the block and append polynomia into queue
        else:
            visited[polyomino] = True
            for pos in positionDict[polyomino]:
                block[pos[0]][pos[1]] = 0
            queue.append(polyomino)
        


    print('Case #{}: {}'.format(case+1, answer))

    

    


        