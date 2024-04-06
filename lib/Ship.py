from lib.Requests import Travel, Collect
from lib.URLS import *
from lib.Graph import Graph

class Ship:    
    def __init__(self, data, graph:Graph):
        self.current_planet_name = data["planet"]["name"]
        self.current_planet_garbage = data["planet"]["garbage"]

        self.capacityX = data["capacityX"]
        self.capacityY = data["capacityY"]

        self.baggage = [['.' for _ in range(self.capacityX)] for _ in range(self.capacityY)]
        self.graph = graph 

        self.number_of_baggage = 1

    def TravelTo(self, destination:str):
        self.graph.dijkstra(self.current_planet_name)
        way = self.graph.FindWay(self.current_planet_name, destination)

        self.graph.IncreaseWay(way)
        way = way[::-1]
        way = way[1:]
        self.current_planet_name = destination
        self.travel_data = Travel(way)

        self.current_planet_garbage = self.travel_data["planetGarbage"]

    def findTrash(self):
        ans = []  

        for x in range(self.capacityX):
            for y in range(self.capacityY):
                if self.baggage[y][x] == (self.number_of_baggage-1):
                    ans.append([x, y])
                    
        return ans
    
    def GetPersent(self):
        vol = self.capacityX * self.capacityY
        counter = 0
        for x in range(self.capacityX):
            for y in range(self.capacityY):
                if self.baggage[y][x] != '.':
                    counter += 1

        return counter / vol


    def TryCollect(self):
        if not self.current_planet_garbage:
            return

        ans = {}
        for i in self.current_planet_garbage:
            res = self.pack_shapes(self.current_planet_garbage[i])
            if res:
                ans[i] = self.findTrash()

        
        if ans:
            Collect(ans)
            print("collected")
        else:
            print("didn't collect")

        return bool(ans)

    def pack_shapes(self, shape):
        def can_place_shape(shape, x, y, rotation):
            for point in shape:
                rotated_point = rotate_point(point, rotation)
                new_x = x + rotated_point[0]
                new_y = y + rotated_point[1]
                if not (0 <= new_x < self.capacityX and 0 <= new_y < self.capacityY):
                    return False
                if self.baggage[new_y][new_x] != '.':
                    return False
            return True

        def place_shape(shape, x, y, rotation):
            for point in shape:
                rotated_point = rotate_point(point, rotation)
                new_x = x + rotated_point[0]
                new_y = y + rotated_point[1]
                self.baggage[new_y][new_x] = self.number_of_baggage

        def rotate_point(point, rotation):
            x, y = point
            if rotation == 90:
                return [-y, x]
            elif rotation == 180:
                return [-x, -y]
            elif rotation == 270:
                return [y, -x]
            else:
                return [x, y]

        placed = False
        for rotation in [0, 90, 180, 270]:
            for y in range(self.capacityX - 1, -1, -1):
                for x in range(self.capacityX - 1, -1, -1):
                    if can_place_shape(shape, x, y, rotation):
                        place_shape(shape, x, y, rotation)
                        self.number_of_baggage += 1
                        placed = True
                        break

                if placed:
                    break
                    
            if placed:
                break
                
        return placed
