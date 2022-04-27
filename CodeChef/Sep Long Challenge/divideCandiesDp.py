def divideCandies(N, K):
    if K == 1:
        summ = N*(N+1)//2
    
    if K == 2:
        summ = N*(N+1)*((2*N)+1)//6
    
    if K == 3:
        summ= N*N*(N+1)*(N+1)//4
    
    dpMatrix = [[[0 for _ in range(summ+1)] for _ in range(summ+1)] for _ in range(N+1)]

    for i in range(N+1):
        for j in range(summ+1):
            for k in range(summ+1):
                if i == 0:
                    dpMatrix[i][j][k] = abs(j-k)
                    continue
                curr = pow(i,K)
                ch1 = float('inf')
                ch2 = float('inf')

                if j+ curr<= summ: ch1 = dpMatrix[i-1][j+curr][k]

                if k+ curr <= summ: ch2 = dpMatrix[i-1][j][k+curr]

    

                dpMatrix[i][j][k] = min(ch1, ch2)
        
    return dpMatrix[N][0][0]

k = int(input())

T = int(input())

for _ in range(T):
    N = int(input())

    print(divideCandies(N, k))
            

            