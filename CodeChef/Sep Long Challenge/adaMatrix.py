from queue import Queue

def getNewMatrix(currMatrix,L,N):
    newMatrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i<L and j < L: newMatrix[i][j] = currMatrix[j][i]
            else: newMatrix[i][j] = currMatrix[i][j]
    
    return newMatrix

try:
    T = int(input())
    for _ in range(T):
        N = int(input())

        goalMatrix = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                goalMatrix[i][j] = (i*N)+ (j+1)

        startMatrix = []


        for _ in range(N):
            row = list(map(int, input().split()))
            startMatrix.append(row)
        
        
        res = 0
        q = Queue()
        q.put(startMatrix)

        doneFlag = False
        while not q.empty() and not doneFlag:
            size = q.qsize()
            for _ in range(size):
                curr = q.get()


                if curr == goalMatrix:
                    doneFlag = True
                    print(res)
                    break

                for i in range(2, N+1):
                    newMatrix = getNewMatrix(curr, i, N)
                    q.put(newMatrix)
                
            res+=1
    
except:
    pass