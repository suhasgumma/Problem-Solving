"Recurse a Given String using recursion"

# Input --> String, size
# Output --> reverse String

# Hypothesis --> reverseStrig(string, size)
# Base Case --> smallest valid Input --> size = 0
# Induction

def reverseStrig(string, size):
    if size == 0:
        return ''
    
    current = string[size-1]

    return current+ reverseStrig(string, size-1)


print(reverseStrig('suhas', 5))