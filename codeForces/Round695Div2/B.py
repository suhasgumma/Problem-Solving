def totalPeaks(arr, n):
    res= 0

    yes = 0

    for i in range(1, n-1):
        lft = arr[i-1]
        right = arr[i+1]
        mid = arr[i]

        rightL = i+2
        leftl = i-2

        if mid > lft and mid > right:
            # print(i)
            res+=1
            
            if leftl >= 0 and rightL< n:
                if arr[leftl] > lft and arr[rightL] > right: yes = 2

            if rightL < n:
                if arr[rightL] > right: yes = max(yes, 1)

            if leftl >=0:
                if arr[leftl] > lft: yes = max(yes, 1)
            
            
            

        if mid < lft and mid < right:
            res+=1

            if leftl >= 0 and rightL< n:
                if arr[leftl] < lft and arr[rightL] < right: yes = 2

            # if rightL < n:
            #     if arr[rightL] < right: yes = max(yes, 1)
    

    if res == 0: return 0

    # if res == 1: return 0

    # print(res,yes)
    
    return res-yes-1


def solve():
    n = int(input())

    arr = list(map(int, input().split()))

    tot = totalPeaks(arr, n)

    print(tot)
    return


t = int(input())




for _ in range(t):
    solve()