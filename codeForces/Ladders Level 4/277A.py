from queue import Queue


def bfs(src, graph, visited):
    q = Queue()

    q.put(src)

    while not q.empty():
        # print("YEAH")
        curr = q.get()

        if curr not in visited:
            visited.add(curr)
            for child in graph[curr]:
                if child not in visited:
                    q.put(child)
    

    # return visited





def solve():
    #Forming Language Graph

    n, m = map(int, input().split())

    lGraph = [[] for _ in range(m+1)]

    zeroGroup = 0

    for i in range(n):
        languageArray = list(map(int, input().split()))

        ln = languageArray[0]+1

        if ln == 1:
            lGraph[0].append(i)
            zeroGroup+=1
        
        for j in range(1, ln):
            lKnown = languageArray[j]

            lGraph[lKnown].append(i)
    

    # print(lGraph)
    

    #Forming Graph Set


    graphSet = [set() for _ in range(n)]

    for i in range(m+1):
        sameLangArray = lGraph[i]

        ln = len(sameLangArray)
 

        for j in range(ln):
            for k in range(j+1, ln):
                src = sameLangArray[j]
                dest = sameLangArray[k]

                graphSet[src].add(dest)
                graphSet[dest].add(src)
    

    # print(graphSet)
    

    visited = set()

    res = 0

    for i in range(n):
        if i not in visited:
            # print("YES", i)
            res+=1
            bfs(i, graphSet, visited)

    


    # print(res)
    if zeroGroup > 0:
        if res == 1:
            print(zeroGroup)
        
        else:
            print(res+zeroGroup-2)
        
        return

    print(res-1)

    return



solve()

    

