def solve(arr, n, x):
    res = 0
    

    if n == 2:
        if arr[1] >= arr[0]: return 0

        if arr[1] > x and x >= arr[0]: return 1

        return -1

    for i in range(n-2):
        left, mid, right = arr[i], arr[i+1], arr[i+2]

        #Everything Fine...
        if left <= mid and mid <= right: continue

        #Peaks

        if left <= mid:
            if right <= left:
                if mid > x and x>= left:
                    res+=1
                    arr[i+1], x = x, arr[i+1]
                    continue
                else: return -1
            
            else:
                if left < x or mid < x or x > right: return -1

                j = i+1

                # print(j)

                while j >= 0 and arr[j] > x:
                    res+=1
                    arr[j], x = x, arr[j]
                    j-=1
        
        #Valleys

        else:
            if left < x or mid < x: return -1

            j = i

            while arr[j] > x:
                res+=1
                arr[j], x = x, arr[j]
                j-=1

        

    return res


t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    arr = list(map(int, input().split()))

    print(solve(arr, n,x))


         

