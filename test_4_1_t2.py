from itertools import product
from math import atan2



def solution(dimensions, your_position, trainer_position, distance):
    x0, y0 = your_position
    hits = dict()

    for position in your_position, trainer_position:
        
        for reflect in product(*[range(-(distance // -d) + 1) for d in dimensions]):
            # print('ref',reflect)
            for quadrant in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                x, y = [
                    (d * r + (d - p if r % 2 else p)) * q
                    for d, p, r, q in zip(dimensions, position, reflect, quadrant)
                ]
                # print('xy',x,y)
                travel = (abs(x - x0) ** 2 + abs(y - y0) ** 2) ** 0.5
                bearing = atan2(x0 - x, y0 - y)
                if travel > distance or bearing in hits and travel > abs(hits[bearing]):
                    continue
                # mark self-hits with a negative travel so we can filter later
                hits[bearing] = travel * (-1 if position == your_position else 1)
    return len([1 for travel in hits.values() if travel > 0])


# import time

# def milliseconds():
#     return int(round(time.time() * 100000))

# start_time = milliseconds()

# x = solution([3,2], [1,1], [2,1], 4)
# # x = solution([10, 10],[4, 4], [3, 3], 5000)

# end_time = milliseconds()


# print(x, end_time-start_time)
import cProfile
cProfile.run("solution([10, 10],[4, 4], [3, 3], 5000)")