'''
2-1
Power hungry
Find the maximum power from panels in the array
'''
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

'''
Test cases
'''
import pytest
def test_pass_1():
    assert solution([2, 0, 2, 2, 0]) == "8"

def test_pass_2():
    assert solution([-2, -3, 4, -5]) == "60"
    
def test_pass_3():
    assert solution([-1, 0, 4]) == "4"

def test_pass_4():
    assert solution([-1, 4]) == "4"

def test_pass_5():
    assert solution([-1, 0]) == "0"

def test_pass_5():
    assert solution([0]) == "0"    

def test_fail_1():
    with pytest.raises(TypeError):
        solution()
