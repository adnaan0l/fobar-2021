from operator import mul

def filter_negatives(xs):
    negatives = [x for x in xs if x < 0]
    if (len(negatives)%2 == 0):
        return negatives
    negatives.remove(max(negatives))
    return filter_negatives(negatives)

def filter_others(xs):
    if [x for x in xs if x > 0]:
        return [x for x in xs if x > 0]
    return [x for x in xs if x == 0]

def solution(xs):
    negatives = filter_negatives(xs)
    numbers = filter_others(xs)

    if len(xs) == 1:
        return str(xs[0])
    return str(reduce(mul, negatives+numbers, 1))

# print(solution([2, 0, 2, 2, 0]))
# print(solution([-2, -3, 4, -5]))
print(solution([-1, 0, 4]))
print(solution([-1, 4]))
print(solution([-1, 0]))
# print(solution([0]))
