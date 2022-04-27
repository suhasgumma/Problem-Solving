def rec(arr, size, me, frnd):
    if size == 0: return abs(me-frnd)

    curr = arr[size-1]

    ch1 = rec(arr, size-1, me+curr, frnd)


    ch2 = rec(arr, size-1, me, frnd+curr)
    
    return min(ch1, ch2)


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




# k = int(input())

# T = int(input())

# for _ in range(T):
#     N = int(input())

#     arr = [pow(i,k) for i in range(1,N+1)]

#     res = rec(arr, N, 0, 0, '')

#     print(res[0])
#     print(res[1])


# print(pow(1,3))

for i in range(100):
    print("yeaah"+ str(i))
    # arr = [j for j in range(1,i+1)]

    # ans1 = rec(arr,i,0,0)
    ans2 = divideCandies(i, 1)

    print(ans2)