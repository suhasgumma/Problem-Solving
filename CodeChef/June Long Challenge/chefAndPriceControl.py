try:
    no_of_test_cases = int(input())

    for i in range(no_of_test_cases):
        N, K = map(int, input().split())
        prices = list(map(int, input().split()))

        revenue_loss = 0

        for i in range(N):
            price = prices[i]
            if price > K:
                revenue_loss+=(price - K)
        
        print(revenue_loss)
    
except:
    pass