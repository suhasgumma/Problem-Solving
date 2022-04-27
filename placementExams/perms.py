def getPerms(string):
    if len(string) == 1:
        return [string]
    
    answer = []
    for i in range(len(string)):
        remaining_string = string[0:i]+ string[i+1:]
        present = string[i]
        perms = getPerms(remaining_string)
        for comb in perms:
            answer.append(present+comb)
    
    return answer

import time

start = time.time()
print(getPerms('su'))
end = time.time()
print(end - start)
