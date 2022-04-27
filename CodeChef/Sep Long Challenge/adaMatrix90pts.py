T = int(input())

for _ in range(T):
    N = int(input())
    
    matrix = []
    
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    tar = [i for i in range(1, N+1)]
    
    rowFirst = matrix[0]
    
    coloumnFirst = [matrix[i][0] for i in range(N)]
    
    res = 0
    
    for i in range(N-1, -1, -1):
        if rowFirst[i] == tar[i]: continue
        
        temp = [rowFirst[j] for j in range(i)]
        
        for j in range(i):
            rowFirst[j] = coloumnFirst[j]
            coloumnFirst[j] = temp[j]
        
        res+=1
    
    print(res)
        

        
        