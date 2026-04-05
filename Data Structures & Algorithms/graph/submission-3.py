class Graph:
    
    def __init__(self):
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.graph and dst in self.graph and dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        else: 
            return False 

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        visit.add(src)
        queue = deque()
        queue.append(src)

        while queue:
            for i in range(len(queue)):
                v = queue.popleft()
                if v == dst:
                    return True 
                
                for n in self.graph[v]:
                    visit.add(n)
                    queue.append(n)

        return False

