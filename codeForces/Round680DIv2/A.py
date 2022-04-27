
t = int(input())

for i in range(t):
    n, x = map(int, input().split())

    a = list(map(int, input().split()))

    b = list(map(int, input().split()))

    if n == 1:
        if a[0]+ b[0] <= x: print("Yes")

        else: print("No")

    else:
        tracker = False
        for j in range(n):
            if a[j] + b[n-j-1] > x:
                tracker = True
                break
        
        if not tracker: print("Yes")

        else: print("No")
    
    if i != t-1:
        s = input()