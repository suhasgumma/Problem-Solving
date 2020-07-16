no_of_families = int(input())
total_extra = 0
total_deficit = 0 
for i in range(no_of_families):
    S,N,K,R = map(int, input().split())
    
    needed = K * ((R**N)-1)/(R-1)

    if S>= needed:
        extra = S- needed
        print('POSSIBLE', int(extra))
        total_extra+= extra

    else:
        deficit = needed - S
        print('IMPOSSIBLE', int(deficit))
        total_deficit+= deficit

if total_extra>= total_deficit:
    print('POSSIBLE')

else:
    print('IMPOSSIBLE')
