t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    past = -1

    gaps = 0

    for i in range(n):
        if arr[i] == 1:
            if past >= 0:
                gaps+= (i-past-1)
                past = i
        
            else: past = i

    
    print(gaps)

