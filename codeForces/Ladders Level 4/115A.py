from queue import Queue

def heightByBfs(src, graph):
    q = Queue()

    q.put(src-1)

    currLevel = 1
    nxtLevel = 0
    level = 0

    while not q.empty():
        curr = q.get()

        currLevel-=1

        for child in graph[curr]:
            q.put(child-1)
            nxtLevel+=1
        

        if currLevel == 0:
            level+=1
            currLevel = nxtLevel
            nxtLevel = 0
    

    return level
    


def solve():
    #Form A Graph

    sources = []

    

    n = int(input())

    

    graph = [[] for _ in range(n)]

    for i in range(n):
        src = int(input())
        

        yeah = False


        if src == -1:
            sources.append(i+1)
        
        else:
            graph[src-1].append(i+1)
        

    
    if yeah: print("What is the damn BUG!!!!!!")

    res = 0


    for src in sources:
        res= max(res, heightByBfs(src, graph))

    
    print(res)

    return


solve()
    
