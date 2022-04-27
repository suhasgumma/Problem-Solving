def solve(l1, r1, l2, r2, k):
    if r2 < l1 or r1 < l2: return 0

    if l1 >= l2 and r2 >= l1:
        if r2 <= r1:
            res = r2-l1+1

            if l1 <= k <=r2:
                res-=1
            
            return res
        
        res = r1-l1+1

        if l1<= k <= r1:
            res-=1
        
        return res
    
    if l2>= l1:
        if r2>= r1:
            res = r1 -l2+1

            if l2 <= k<= r1:
                res-=1
            
            return res
    
        res = r2 - l2+1

        if l2 <= k<= r2:
            res -=1
        
        return res


l1, r1, l2, r2, k = map(int, input().split())


print(solve(l1, r1, l2, r2, k))
