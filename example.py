from map import Map, load_map
from pathfinder import Pathfinder

map_40 = load_map()
start = 8
goal = 27
pathfinder = Pathfinder(map_40, start, goal)
path = pathfinder.path

map_40.draw(path)
