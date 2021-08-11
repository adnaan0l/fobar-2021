from itertools import product
from math import atan2
import cProfile

class TrainerFight():

    def __init__(self, dimensions, your_position, trainer_position, distance):

        self.player_pos = your_position
        self.trainer_pos = trainer_position
        self.distance = distance
        self.dim = dimensions
        self.t_points = {}
        self.p_points = {}
        self.edge_vertices = {}

    def get_position(self, position):        
        x_list = set()
        y_list = set()

        x = position[0]
        y = position[1]

        edge_vertices = [(0,0), (0,self.dim[1]), (self.dim[0],0), (self.dim[0],self.dim[1])]
        self.edge_vertices = {self.get_angle(edge) : edge for edge in edge_vertices}

        while x <= self.distance or y <= self.distance :
            x_list.add(x)
            x+=2*self.dim[0]
            y_list.add(y)
            y+=2*self.dim[1]
        x = (2*self.dim[0])-position[0]
        y = (2*self.dim[1])-position[1]
        while x <= self.distance or y <= self.distance:
            x_list.add(x)
            x+=2*self.dim[0]
            y_list.add(y)
            y+=2*self.dim[1]  

        all_angles = {}

        q1_points = list(product(x_list, y_list))
        all_points = [[(point[0],point[1]), (point[0],-point[1]), (-point[0],-point[1]), (-point[0],point[1])] for point in q1_points]

        for points in all_points:
            for point in points:
                angle = self.get_angle(point)
                if angle in all_angles:
                    if (abs(all_angles[angle][0]),abs(all_angles[angle][1])) > (abs(point[0]),abs(point[1])):                    
                        all_angles[angle] = point
                else:
                    all_angles[angle] = point
        return all_angles
    
    def get_angle(self, node):
        return atan2((self.player_pos[0] - node[0]), (self.player_pos[1] - node[1]))

    def get_distance(self, node):
        return abs(node[0]-self.player_pos[0]) ** 2 + abs(node[1]-self.player_pos[1]) ** 2

    def max_distance(self, node):
        # print(node)
        # print(self.get_distance(node))
        if self.get_distance(node) >= self.distance ** 2:
            return True
        return False

    def hitting_vertex(self, node):
        angle = self.get_angle(node) 
        if (angle in self.edge_vertices) and (self.get_distance(self.edge_vertices[angle]) < self.get_distance(node) ):
            return True
        return False

    def hitting_guard(self, node):
        angle = self.get_angle(node)
        if self.get_distance(self.p_points[angle]) != 0 and self.get_distance(self.p_points[angle]) < self.get_distance(node):
            return True
        return False

    def get_directions(self):
        directions = set()
        p_pos_x = self.player_pos[0]
        p_pos_y = self.player_pos[1]
        count=0
        for t_point in self.t_points.values():
            angle = self.get_angle(t_point)
            if self.get_distance(t_point) == 0:
                directions.add(t_point)
            if not self.max_distance(t_point) and not self.hitting_vertex(t_point):
                count+=1
                if angle in self.p_points.keys():
                    if not self.hitting_guard(t_point):
                        directions.add(angle)
                else:
                    directions.add(angle)
            print(len(directions))
        return len(directions)

def solution(dimensions, your_position, trainer_position, distance):
    fight = TrainerFight(dimensions, your_position, trainer_position, distance)
    fight.t_points = fight.get_position(fight.trainer_pos)
    fight.p_points = fight.get_position(fight.player_pos)
    return fight.get_directions()


# print(solution([3,2], [1,1], [2,1], 4))
# print(solution([300,275], [150,150], [185,100], 500))

# def test_case_1():
#     assert solution([3,2], [1,1], [2,1], 4) == 7
# def test_case_2():
#     assert solution([300,275], [150,150], [185,100], 500) == 9
# def test_case_3():
#     assert solution([20, 20], [2, 2], [2, 4], 5) == 2
# def test_case_4():
#     assert solution([2,5],[1,2],[1,4],11) == 27
# def test_case_5():
#     assert solution([23,10], [6, 4], [3,2], 23) == 8
# def test_case_6():
#     assert solution([2,3], [1,1], [1,2], 5) == 13
# def test_case_7():
#     assert solution([10, 10],[4, 4], [3, 3], 5000) == 739323

# import time

# def milliseconds():
#     return int(round(time.time() * 100000))

# start_time = milliseconds()

# x = solution([10, 10],[4, 4], [3, 3], 5000)

# end_time = milliseconds()


# print(x, end_time-start_time)

cProfile.run("solution([10, 10],[4, 4], [3, 3], 5000)")