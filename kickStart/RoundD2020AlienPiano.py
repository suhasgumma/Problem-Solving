def pianoConversion(array, idx, prev):
    if idx == len(array):
        return 0

    mini = float('inf')
    
    if idx == 0:
        for i in range(1, 5):
            mini = min(mini, pianoConversion(array, idx+1, i))
        
        return mini
    
    el = array[idx]

    if el > array[idx-1]:
        for i in range(1, 5):
            if i > prev:
                mini = min(mini, pianoConversion(array, idx+1, i))
            else:
                mini = min(mini, 1+pianoConversion(array, idx+1, i))
    
    if el < array[idx-1]:
        for i in range(1, 5):
            if i < prev:
                mini = min(mini, pianoConversion(array, idx+1, i))
            else:
                mini = min(mini, 1+pianoConversion(array, idx+1, i))

    if el == array[idx-1]:
        for i in range(1, 5):
            if i == prev:
                mini = min(mini, pianoConversion(array, idx+1, i))
            else:
                mini = min(mini, 1+pianoConversion(array, idx+1, i))

    return mini


T  = int(input())

for i in range(T):
    K = int(input())

    notes = list(map(int, input().split()))

    answer = pianoConversion(notes, 0, 0)

    print(f"Case #{i+1}: {answer}")
    
