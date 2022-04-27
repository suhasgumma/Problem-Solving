def solve():
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    a, b= 0, k

    dpArr = [arr[0] for _ in range(n)]

    for i in range(1, n):
        dpArr[i] = arr[i]+ dpArr[i-1]

    
    maxSum = dpArr[(2*k)-1]
    
    for i in range(n-k-1):
        for j in range(i+k, n-k+1):

            if i > 0:
                sum1 = dpArr[i+k-1] - dpArr[i-1]
            
            else: sum1 = dpArr[i+k-1]

            sum2 = dpArr[j+k-1] - dpArr[j-1]

            summ = sum1+ sum2

            if summ > maxSum:
                maxSum = summ
                a = i
                b = j
    

    print(a+1, b+1)

    return



solve()