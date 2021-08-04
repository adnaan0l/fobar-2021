'''
3-2
'''
import time
from operator import itemgetter

class NodeInfo:

    def __init__(self, map):

        self.map = map
        self.curr_node = (0, 0)
        self.dest = (len(map)-1, len(map[0])-1)
        self.node_dict = {}
        self.hist_list = []
        self.power = 1
        self.maxx = len(self.map[0])-1
        self.maxy = len(self.map)-1
        self.min = 0

    def create_dict(self,map):
        node_dict = {}
        for x in range(len(map[0])):
            for y in range(len(map)):
                self.node_dict[(y, x)] = self.get_neighbours(y,x)

    def check_passable(self, node):
        y, x = node
        if self.map[y][x] == 0 and node not in self.hist_list:
            return True
        elif self.power == 1 and (self.map[y][x] == 1 and self.map[y+1][x] == 0) or (self.map[y][x] == 1 and self.map[y][x+1] == 0):
            self.power=0
            return True   
        return False

    def get_neighbours(self, y, x):
        neighbours = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
        sorted_neighbours = [neighbour for neighbour in neighbours if 0 <= neighbour[0] <= self.maxy and 0 <= neighbour[1] <= self.maxx]
        sorted_neighbours.sort(key=itemgetter(0,1), reverse=True)
        return sorted_neighbours
            
    def find_path(self):
        if self.curr_node == self.dest:
            self.hist_list.append(self.curr_node)
            return len(self.hist_list)
        for path in self.node_dict[(self.curr_node)]:
            if self.check_passable(path):
                self.hist_list.append(self.curr_node)
                self.curr_node = path
                return self.find_path()
        return 0         

def solution(map):
    node = NodeInfo(map)
    node.create_dict(map)
    nodes = node.find_path()
    return nodes

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
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

route_length = solution(array)
end_time = milliseconds()

print(route_length)
print(end_time-start_time)