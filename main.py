import json
import requests
import time

#########################
#### DATA STRUCTURES ####
#########################
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

##################
#### DIJKSTRA ####
##################
def dijkstra(graph, start, end):
    f = PriorityQueue()
    f.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not f.empty():
        current = f.get()
        print(current, '\n')

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

#####################
#### CALL TO API ####
#####################
def sendpayload(url, payload):
    r = requests.get(url, params = payload)
    if r.status_code != 200:
        print('HTTP status code {} received, program terminated.'.format(r.status_code))
    else:
        try:
            result = json.loads(r.text)
            print(result)
            return result
        except ValueError:
            print('Error while parsing JSON response, program terminated.')

#######################
#### GRAPH HANDLER ####
#######################
def add2graph(r, graph):
    for isrc, src in enumerate(r['origin_addresses']):
        if src not in graph.vertsd:
            graph.addvertex(src)
        for idst, dst in enumerate(r['destination_addresses']):
            row = r['rows'][isrc]
            cell = row['elements'][idst]
            if dst not in graph.vertsd:
                graph.addvertex(dst)
            graph.addedge(src, dst, cell['distance']['value'])
    return graph


##############
#### MAIN ####
##############
if __name__ == '__main__':
    key = 'AIzaSyB4JIdwOtl_8OLuw-NMr6EZ-3jz6emfKAc'
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    #### Sacar los pueblos de pueblos.txt ####
    file = open('lib/pueblos.txt', 'r')
    o1 = file.readline()
    d1 = file.readline()
    o2 = file.readline()
    d2 = file.readline()
    o3 = file.readline()
    d3 = file.readline()
    o4 = file.readline()
    d4 = file.readline()
    o5 = file.readline()
    d5 = file.readline()
    o6 = file.readline()
    d6 = file.readline()
    file.close()

    print(len(o1.split('|')) + len(d1.split('|')))
    print(len(o2.split('|')) + len(d2.split('|')))
    print(len(o3.split('|')) + len(d3.split('|')))
    print(len(o4.split('|')) + len(d4.split('|')))
    print(len(o5.split('|')) + len(d5.split('|')))
    print(len(o6.split('|')) + len(d6.split('|')), '\n')

    #### Armar las payloads para la API ####
    payload1 = {
        'origins': o1,
        'destinations': d1,
        'key': key,
        'mode': 'driving'
    }
    payload2 = {
        'origins': o2,
        'destinations': d2,
        'key': key,
        'mode': 'driving'
    }
    payload3 = {
        'origins': o3,
        'destinations': d3,
        'key': key,
        'mode': 'driving'
    }
    payload4 = {
        'origins': o4,
        'destinations': d4,
        'key': key,
        'mode': 'driving'
    }
    payload5 = {
        'origins': o5,
        'destinations': d5,
        'key': key,
        'mode': 'driving'
    }
    payload6 = {
        'origins': o6,
        'destinations': d6,
        'key': key,
        'mode': 'driving'
    }

    #### Obtener las distancias de Distance Matrix API ###
    t = time.clock()
    r1 = sendpayload(url, payload1)
    r2 = sendpayload(url, payload2)
    r3 = sendpayload(url, payload3)
    r4 = sendpayload(url, payload4)
    r5 = sendpayload(url, payload5)
    r6 = sendpayload(url, payload6)
    print(time.clock(), ' time taked to call the API \n')

    #### Crear el grafo con todos los pueblos ####
    t = time.clock()
    graph = Graph()
    graph = add2graph(r1, graph)
    graph = add2graph(r2, graph)
    graph = add2graph(r3, graph)
    graph = add2graph(r4, graph)
    graph = add2graph(r5, graph)
    graph = add2graph(r6, graph)
    print(time.clock(), ' time taked to add to Graph \n')

    t = time.clock()
    camino, costo = dijkstra(graph, 'Tecate, Baja California, Mexico', 'Isla Mujeres, Quintana Roo, Mexico')
    print(time.clock(), ' time taked Dijkstra \n')

    file = open('lib/resultados.txt', 'w')
    file.write(camino)
    file.write(costo)
    file.close()