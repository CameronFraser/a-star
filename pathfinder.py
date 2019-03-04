from collections import defaultdict
import math


class Pathfinder:
    def __init__(self, map, start=None, goal=None):
        # Set appropriate defaults
        self.map = map
        self.start = start
        self.goal = goal
        self.closedSet = set()  # already evaluated nodes
        self.openSet = {start}  # frontier
        self.cameFrom = {}

        # the cost of the start to move to start is 0 so we can set start to 0 and rest to inf
        gScore = defaultdict(lambda: math.inf)
        gScore[self.start] = 0
        self.gScore = gScore
        # the fScore of the start will just be the heuristic cost estimate and rest set to inf
        fScore = defaultdict(lambda: math.inf)
        fScore[start] = self.heuristic_cost_estimate(start)
        self.fScore = fScore
        # run search
        self.path = self.run_search()

    def reconstruct_path(self, current):
        total_path = [current]
        while current in self.cameFrom.keys():
            current = self.cameFrom[current]
            total_path.append(current)
        return total_path

    def run_search(self):
        # while the open set is not empty
        while not self.is_open_empty():
            current = self.get_current_node()
            # if we're at the goal then reconstruct the path and return the path
            if current == self.goal:
                self.path = [x for x in reversed(
                    self.reconstruct_path(current))]
                return self.path
            else:
                # else remove the current node from the openset and add to closedset
                self.openSet.remove(current)
                self.closedSet.add(current)
            # Check out all your neighbors
            for neighbor in self.get_neighbors(current):
                # if your neighbor has been evaluated already go to next iteration
                if neighbor in self.closedSet:
                    continue
                # if your neighbor is not in the openSet add them
                if not neighbor in self.openSet:
                    self.openSet.add(neighbor)
                # if the tentative cost to travel to your neighbor is greater than or equal to neighbor cost
                # continue to next iteration
                if self.get_tentative_gScore(current, neighbor) >= self.get_gScore(neighbor):
                    continue
                # otherwise this is the best path to take, record it
                self.record_best_path_to(current, neighbor)
        print("No Path Found")
        self.path = None
        return False

    def is_open_empty(self):
        return len(self.openSet) == 0

    def get_current_node(self):
        # node with the lowest fScore in the openSet is the node we want to look at
        lowestfNode = None
        lowestfValue = None
        for val in self.openSet:
            if lowestfNode == None:
                lowestfNode = val
                lowestfValue = self.calculate_fscore(lowestfNode)
            else:
                if self.calculate_fscore(val) < lowestfValue:
                    lowestfNode = val
                    lowestfValue = self.calculate_fscore(lowestfNode)
        return lowestfNode

    def get_neighbors(self, node):
        return self.map.roads[node]

    def get_gScore(self, node):
        return self.gScore[node]

    def distance(self, node_1, node_2):
        # euclidean distance formula
        x1, y1 = self.map.intersections[node_1]
        x2, y2 = self.map.intersections[node_2]

        dx = x1 - x2
        dy = y1 - y2
        dist = math.sqrt(dx**2 + dy**2)
        return dist

    def get_tentative_gScore(self, current, neighbor):
        return self.get_gScore(current) + self.distance(current, neighbor)

    def heuristic_cost_estimate(self, node):
        return self.distance(self.goal, node)

    def calculate_fscore(self, node):
        gScore = self.get_gScore(node)
        cost = self.heuristic_cost_estimate(node)
        fScore = gScore + cost

        return fScore

    def record_best_path_to(self, current, neighbor):
        self.cameFrom[neighbor] = current
        self.gScore[neighbor] = self.get_tentative_gScore(current, neighbor)
        self.fScore[neighbor] = self.calculate_fscore(neighbor)
