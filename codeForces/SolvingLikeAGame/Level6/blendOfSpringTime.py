def solve(garden):
    n = len(garden)

    for i in range(1, n-1):
        hashSet = set()

        hashSet.add(garden[i-1])
        hashSet.add(garden[i])
        hashSet.add(garden[i+1])

        if "A" in hashSet and 'B' in hashSet and 'C' in hashSet: return "Yes"
    
    return "No"


garden = input()

print(solve(garden))