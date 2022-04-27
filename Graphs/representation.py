class Node:
    def __init__(self, ver):
        self.ver = ver
        self.next = None


class Graph:
    def __init__(self, V):
        self.adjacencyList = [None for _ in range(V)]
    

    def addEdge(self, u, v):
        if self.adjacencyList[u] == None:
            self.adjacencyList[u] = Node(v)
        else:
            temp = self.adjacencyList[u]
            while temp.next!= None:
                temp = temp.next
            
            temp.next = Node(v)

        if self.adjacencyList[v] == None:
            self.adjacencyList[v] = Node(u)
        else:
            temp = self.adjacencyList[v]
            while temp.next!= None:
                temp = temp.next
            
            temp.next = Node(u)
    

g = Graph(5)

g.addEdge(1,3)
g.addEdge(2, 4)
g.addEdge(0,1)
g.addEdge(1, 2)

# for i in range(len(g.adjacencyList)):
#     temp = g.adjacencyList[i]
#     while temp!= None:
#         print(temp.ver,)
#         temp = temp.next
#     print("*****************")





