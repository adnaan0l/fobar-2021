import itertools
from math import atan2

class TrainerFight():

    def __init__(self, dimensions, your_position, trainer_position, distance):

        self.player_pos = your_position
        self.trainer_pos = trainer_position
        self.distance = distance
        self.dim = dimensions
        self.t_points = {}
        self.p_points = {}

    def get_position(self, position):        
        x_list = set()
        y_list = set()

        x = position[0]
        y = position[1]

        while x <= self.distance or y <= self.distance:
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

        q1_points = list(itertools.product(x_list, y_list))
        q2_points = [(point[0],-point[1]) for point in q1_points]
        q3_points = [(-point[0],-point[1]) for point in q1_points]
        q4_points = [(-point[0],point[1]) for point in q1_points]
        all_points = q1_points+q2_points+q3_points+q4_points
        
        for point in all_points:
            angle = self.get_angle(point)
            if angle in all_angles:
                if (abs(all_angles[angle][0]),abs(all_angles[angle][1])) > (abs(point[0]),abs(point[1])):                    
                    all_angles[angle] = point
            else:
                 all_angles[angle] = point
        return all_angles

    def get_angle(self, node):
        return str(atan2((node[1]-self.player_pos[0]),(node[0]-self.player_pos[1])))

    def get_distance(self, node):
        return pow(node[0]-self.player_pos[0],2)+pow(node[1]-self.player_pos[1],2)

    def get_directions(self):
        directions = set()
        p_pos_x = self.player_pos[0]
        p_pos_y = self.player_pos[1]
        for t_point in self.t_points.values():
            if not self.get_distance(t_point) > pow(self.distance,2):
                angle = str(atan2((t_point[1]-p_pos_y),(t_point[0]-p_pos_x)))
                if angle in self.p_points.keys():
                    if self.get_distance(self.p_points[angle]) == 0 or self.get_distance(self.p_points[angle]) > self.get_distance(t_point):
                        directions.add(angle)
                else:
                    directions.add(angle)
        return len(directions)

def solution(dimensions, your_position, trainer_position, distance):
    fight = TrainerFight(dimensions, your_position, trainer_position, distance)
    fight.t_points = fight.get_position(fight.trainer_pos)
    fight.p_points = fight.get_position(fight.player_pos)
    return fight.get_directions()

print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))