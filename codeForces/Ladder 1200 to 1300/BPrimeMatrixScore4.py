import math 
  

def isPrime(n): 
      
    # Corner cases  
    if(n <= 1): 
        return False
    if(n <= 3): 
        return True
    
    if(n % 2 == 0 or n % 3 == 0): 
        return False
      
    for i in range(5,int(math.sqrt(n) + 1), 6):  
        if(n % i == 0 or n % (i + 2) == 0): 
            return False
      
    return True
  

def nextPrime(N): 
  
    if (N <= 1): 
        return 2
  
    prime = N 
    found = False
    
    while(not found): 
        prime = prime + 1
  
        if(isPrime(prime) == True): 
            found = True
  
    return prime 


def nextPrimeList(n):
    arr = [False]* (n+1)

    for i in range(2, n+1):
        if not arr[i]:
            j = 2
            while j*i <=n:
                arr[j*i] = True
                j+=1
    
    res = [2]*(n+1)

    i = 2

    while i <= n:
        if not arr[i]: res[i] = i

        else:
            j = i

            while j <=n and arr[j] == True:
                j+=1

            # print(i, j)
            if j >n:
                nxt = nextPrime(j-1)
                # print(nxt)
                res[i] = nxt
            else:
                # print(i, j)
                res[i] = j
        
        # print(res)

        i+=1
     
        
    
    return res




def solve(matrix, n, m):
    maxim = matrix[0][0]

    for i in range(n):
        for j in range(m):
            maxim = max(maxim, matrix[i][j])
    
    
    
    nxtPList = nextPrimeList(maxim)

    # print(nxtPList)
    
    scores = [[0 for _ in range(m)] for _ in range(n)]

    # print(scores)

    for i in range(n):
        for j in range(m):
            scores[i][j] = nxtPList[matrix[i][j]] -  matrix[i][j]
    
    res = math.inf

    for i in range(n):
        rowScore = 0
        for j in range(m):
            rowScore+= scores[i][j]
        
        
        res = min(res, rowScore)
    
    for i in range(m):
        coloumnScore = 0
        for j in range(n):
            coloumnScore+= scores[j][i]
        # print(coloumnScore)
        res =min(res, coloumnScore)
    
    # print(scores)
    
    return res


n, m = map(int, input().split())

matrix = []

for _ in range(n):
    row=  list(map(int, input().split()))
    matrix.append(row)

print(solve(matrix, n, m))


# print(nextPrimeList(4))


    

