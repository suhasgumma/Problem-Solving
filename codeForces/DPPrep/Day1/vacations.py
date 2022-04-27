memo = {}

def solveByRec(arr, start, n, prev):
    if start == n: return 0

    if (start, prev) in memo: return memo[(start, prev)]

    curr = arr[start]

    if curr == 0:
        ans = 1+ solveByRec(arr, start+1, n,0)
        memo[(start, prev)] = ans
        return ans
    
    if curr == 1:
        if prev == 1:
            ans = 1+ solveByRec(arr, start+1, n,0)
            memo[(start, prev)] = ans
            return ans
        
        op1 = 1+ solveByRec(arr, start+1, n,0)
        op2 = solveByRec(arr, start+1, n,1)

        ans = min(op1, op2)
        memo[(start, prev)] = ans
        return ans
    
    if curr == 2:
        if prev ==2:
            ans = 1+ solveByRec(arr, start+1, n,0)
            memo[(start, prev)] = ans
            return ans
        
        op1 = 1+ solveByRec(arr, start+1, n,0)
        op2 = solveByRec(arr, start+1, n,2)

        ans = min(op1, op2)
        memo[(start, prev)] = ans
        return ans
    
    if curr == 3:
        if prev == 2:
            op1 = 1+ solveByRec(arr, start+1, n,0)
            op2 = solveByRec(arr, start+1, n,1)

            ans = min(op1, op2)
            memo[(start, prev)] = ans
            return ans
        
        if prev == 1:
            op1 = 1+ solveByRec(arr, start+1, n,0)
            op2 = solveByRec(arr, start+1, n,2)

            ans = min(op1, op2)
            memo[(start, prev)] = ans
            return ans
        
        op1 = 1+ solveByRec(arr, start+1, n,0)
        op2 = solveByRec(arr, start+1, n,1)
        op3 = solveByRec(arr, start+1, n,2)

        ans = min(op1, op2, op3)
        memo[(start, prev)] = ans
        return ans


n = int(input())
arr = list(map(int, input().split()))

print(solveByRec(arr, 0, n, 0))
        



