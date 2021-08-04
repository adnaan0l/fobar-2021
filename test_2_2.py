'''
2-2
Pass the Coded Message
You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or 
all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 
1 to 9 digits. The same digit may appear multiple times in the list, but each element in the list may only be used once.

'''
from itertools import combinations

def check_mod(mod, l):
    while (mod < 10):
        if mod in l:
            l.remove(mod)
            return l
        else:
            mod+=3
    raise Exception

def check_pairs(mod, l):
    while (mod < 10):
        pairs = [pair for pair in combinations(l, 2) if sum(pair) == mod]
        if pairs:
            l.remove(pairs[0][0])
            l.remove(pairs[0][1])
            return l
        else:
            mod+=3
    raise Exception
    
def get_divisible(l):
    mod = sum(l) % 3 
    if mod == 0:
        return l
    else:
        try: 
            return check_mod(mod, l)
        except:
            return check_pairs(mod, l)
            
def get_largest(l):
    return ''.join([str(integer) for integer in l])

def solution(l):
    l = sorted(l, reverse=True)

    try:
        div_l = get_divisible(l)
    except:
        return 0
    else:
        return get_largest(div_l)


print(solution([3, 1, 4, 1, 5, 9]))
print(solution([5,8,8,5,8,8,2,2]))
# print(solution([9,7,9,8,7,8,9,8,8]))