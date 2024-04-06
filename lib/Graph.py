import heapq

class Graph:
    def __init__(self, graph):
        vertex_set = set()
        self.graph = { }

        for edge in graph:
            if(edge[0] not in vertex_set):
                vertex_set.add(edge[0])
                self.graph[edge[0]] = {}


            if(edge[1] not in vertex_set):
                vertex_set.add(edge[1])
                self.graph[edge[1]] = {}

            self.graph[edge[0]][edge[1]] = edge[2]


    def increase_edge(self, from_, to_):
        const = 10
        self.graph[from_][to_] += const

    def IncreaseWay(self, way:list):
        for vert in way:
            if(vert == way[-1]):
                break
            
            pred = self.previous[vert]
            self.increase_edge(pred, vert)


    def dijkstra(self, start):
        self.distances = {node: float('infinity') for node in self.graph}
        self.distances[start] = 0
        self.previous = {node: None for node in self.graph}
        
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
        
            if current_distance > self.distances[current_vertex]:
                continue
                
            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight
                if distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    self.previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))
                    
    
    def FindWay(self, from_, to_):
        
        way = [to_]

        while (to_ != from_):
            if(to_ == None):
                return []
            
            to_ = self.previous[to_]
            way.append(to_)

        return way
