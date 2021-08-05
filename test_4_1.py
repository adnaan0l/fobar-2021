class TrainerFight():

    def __init__(self, dimensions, your_position, trainer_position, distance):

        self.player = (0,0)
        self.trainer = trainer_position - your_position
        self.distance = distance
        self.dimensions = dimensions

    def get_guard_pos(self, g_pos, max_dist, dim):
        offset = (2*(dim[0] - g_pos[0]), 2*(dim[1] - g_pos[1]))

        pos_list = []

        while g_pos[0]<=max_dist:
            array=[]
            while g_pos[1]<=max_dist:
                array.append((g_pos[0], g_pos[1]))
                g_pos = (g_pos[0], g_pos[1]+offset[1])
            pos_list.append(array)
            g_pos = (g_pos[0]+offset[0], g_pos[1])
        print(pos_list)



def solution(dimensions, your_position, trainer_position, distance):


print(get_guard_pos((2,1), 4, (3,2)))