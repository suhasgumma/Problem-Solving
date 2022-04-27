def solve(rects, n):
    prev = max(rects[0][0], rects[0][1])

    for i in range(1,n):
        mini = min(rects[i])
        maxi = max(rects[i])

        # print(mini, maxi)

        if maxi <= prev:
            prev = maxi
        
        elif mini<= prev:
            prev = mini
        
        else:
            return "NO"
    
    return "YES"

n = int(input())

rects = []

for _ in range(n):
    w,h = map(int, input().split())

    rects.append((w, h))

print(solve(rects, n))
