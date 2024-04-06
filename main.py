from lib.Requests import Get
from lib.Graph import Graph
from lib.Ship import Ship
from lib.URLS import *
from time import sleep, time

visited = set()

def main(timer):
    try:
        init_request = Get(UNIVERSE)
        ship = Ship(init_request["ship"], graph=Graph(init_request["universe"]))

        try:
            ship.TravelTo("Eden")
        except:
            print("Already in Eden")

        stack = []

        def dfs(graph, visited, v):
            visited.add(v)
            stack.append(v)  # Add the current node to the stack

            for neighbor in graph[v]:
                if neighbor not in visited:
                    dfs(graph, visited, neighbor)

        visited = set()
        dfs(ship.graph.graph, visited, ship.current_planet_name)
        stack.pop(0)
        
        stack.reverse()
        # Reverse the stack to get the correct order of planets to visit
        
        for planet in stack:
            if planet in visited:
                continue

            visited.add(planet)
            print("Going to:", planet)
            ship.TravelTo(planet)
            ship.TryCollect()

            percent = ship.GetPersent()
            
            print(str(percent)[:4] + "%", "going to Eden")
            ship.TravelTo("Eden")
            ship.baggage = [['.' for _ in range(ship.capacityX)] for _ in range(ship.capacityY)]
            ship.number_of_baggage = 1
            

            sleep(timer)
    except:
        timer += 0.05
        main(timer)

if __name__ == "__main__":
    # main(0.05)
    print(Get(UNIVERSE))