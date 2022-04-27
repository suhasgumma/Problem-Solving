from queue import Queue
try:
    T = int(input())
    for _ in range(T):
        N = int(input())
        V = list(map(int, input().split()))

        mini = float('inf')
        maxi = -float('inf')

        for i in range(N):
            q = Queue()
            infected = set()
            q.put((i,0))
            infected.add(i)

            while not q.empty():
                size = q.qsize()

                for _ in range(size):
                    curr = q.get()

                    for j in range(N):
                        if j not  in infected:
                            if V[j] - V[curr[0]] == 0: newT = -1
                            else: newT = (curr[0]- j)/(V[j] - V[curr[0]])

                            if newT> curr[1]:
                                q.put((j, newT))
                                infected.add(j)

            
            l = len(infected)

            maxi = max(maxi, l)
            mini = min(mini, l)

        
        print(mini,maxi)
except: pass