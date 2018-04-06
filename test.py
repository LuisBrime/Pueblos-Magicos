import heapq
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def addneighbor(self, n, weight = 0):
        self.adjacent[n] = weight

    def getconnections(self):
        return self.adjacent.keys()

    def getid(self):
        return self.id

    def getweight(self, n):
        return self.adjacent[n]

class Graph:
    def __init__(self):
        self.vertsd = {}
        self.v = 0

    def addvertex(self, n):
        self.v = self.v + 1
        new_vertex = Vertex(n)
        self.vertsd[n] = new_vertex
        return new_vertex

    def getvertex(self, n):
        if n in self.vertsd:
            return self.vertsd[n]
        else:
            return None

    def addedge(self, frm, to, cost = 0):
        if frm not in self.vertsd:
            self.addvertex(frm)
        if to not in self.vertsd:
            self.addvertex(to)

        self.vertsd[frm].addneighbor(self.vertsd[to], cost)
        self.vertsd[to].addneighbor(self.vertsd[frm], cost)

    def getvertices(self):
        return self.vertsd.keys()





def dijkstra(graph, start, end):
    f = PriorityQueue()
    f.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not f.empty():
        current = f.get()

        if current == end:
            break

        for n in graph.getvertex(current).getconnections():
            new_cost = cost_so_far[current] + graph.getvertex(current).getweight(n)
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                priority = new_cost
                f.put(n, priority)
                came_from[n] = current
    return came_from, cost_so_far



if __name__ == '__main__':
    g = Graph()

    g.addedge('a', 'b', 10)
    g.addedge('a', 'c', 20)
    g.addedge('b', 'c', 5)
    g.addedge('b', 'd', 30)
    g.addedge('c', 'd', 5)

    came, cost = dijkstra(g, 'a', 'd')
    print(came)
    print(cost)