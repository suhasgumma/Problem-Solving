def mcm(array, i, j):
    if i>= j:
        return 0
    
    mini = float('inf')
    miniK = -1

    for k in range(i, j):
        left = mcm(array, i, k)
        right = mcm(array, k+1, j)

        cost = left+right+ (array[i-1]*array[k]*array[j])

        if cost < mini:
            mini = cost
            miniK = k
    
    print(miniK)

    return mini


print(mcm([40, 20, 30, 10, 30],1, 4))