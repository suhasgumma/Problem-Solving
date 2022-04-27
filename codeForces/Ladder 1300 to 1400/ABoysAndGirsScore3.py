def solve():
    n, m = map(int, input().split())

    if n > m:
        strFront = m * "BG"
        strEnd = (n-m)* "B"
    
    else:
        strFront = n* "GB"
        strEnd = (m-n)* "G"
    
    print(strFront+ strEnd)

    return


solve()