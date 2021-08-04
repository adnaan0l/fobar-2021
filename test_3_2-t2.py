from collections import deque
import time

class Node:

    def __init__(self, x, y, power, grid):
        self.x = x
        self.y = y;
        self.power = power
        self.grid = grid

    def __hash__(self):
        return self.x ^ self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.power == other.power

    def get_neighbors(self):
        neighbors = []
        x = self.x
        y = self.y
        power = self.power
        grid = self.grid
        rows = len(grid)
        columns = len(grid[0])

        if x > 0:
            wall = grid[y][x - 1] == 1
            if wall:
                if power > 0:
                    neighbors.append(Node(x - 1, y, power - 1, grid))
            else:
                neighbors.append(Node(x - 1, y, power, grid))

        if x < columns - 1:
            wall = grid[y][x + 1] == 1
            if wall:
                if power > 0:
                    neighbors.append(Node(x + 1, y, power - 1, grid))
            else:
                neighbors.append(Node(x + 1, y, power, grid))

        if y > 0:
            wall = grid[y - 1][x] == 1
            if wall:
                if power > 0:
                    neighbors.append(Node(x, y - 1, power - 1, grid))
            else:
                neighbors.append(Node(x, y - 1, power, grid))

        if y < rows - 1:
            wall = grid[y + 1][x]
            if wall:
                if power > 0:
                    neighbors.append(Node(x, y + 1, power - 1, grid))
            else:
                neighbors.append(Node(x, y + 1, power, grid))

        return neighbors


class GridEscapeRouter:

    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.power = 1


def solution(map):

    router = GridEscapeRouter(map)

    source = Node(0, 0, router.power, map)
    queue = deque([source])
    distance_map = {source: 1}

    while queue:
        current_node = queue.popleft()

        if current_node.x == router.columns - 1 and\
            current_node.y == router.rows - 1:
            return distance_map[current_node]

        for child_node in current_node.get_neighbors():
            if child_node not in distance_map.keys():
                distance_map[child_node] = distance_map[current_node] + 1
                queue.append(child_node)

    return 0

def milliseconds():
    return int(round(time.time() * 1000))

start_time = milliseconds()
array = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

route_length = solution(array)
end_time = milliseconds()

print(route_length)
print(end_time-start_time)