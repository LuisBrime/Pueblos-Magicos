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

class Graph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]

    def neighborscost(self, next):
        return self.edges[next].cost

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

        for n in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.neighborscost(n)
            if n not in cost_so_far or new_cost < cost_so_far[n]:
                cost_so_far[n] = new_cost
                priority = new_cost
                f.put(n, priority)
                came_from[n] = current

    return came_from, cost_so_far
