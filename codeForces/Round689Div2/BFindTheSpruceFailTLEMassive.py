def isSpruce(mat, n, m, x, y, h):
    if x+h > n or y+h > m or y-h+1 < 0: return False

    for i in range(h):
        for j in range(i+1):
            if mat[x+i][y+j] != '*' or mat[x+i][y-j] != '*':
                return False
    
    return True


def countSpruce(mat, n, m):
    h = min(n, m-m//2)

    res = 0

    for i in range(1,h+1):
        for x in range(n):
            for y in range(m):
                # print(x, y)
                if isSpruce(mat, n, m, x, y, i):
                    res+=1
                    # print(x, y, i)
        
        # print(res)
    

    return res



t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    mat = []

    for i in range(n):
        r=  input()

        mat.append(r)
    
    print(countSpruce(mat, n, m))