import random

class triplePairs():

    def __init__(self):
        pair_list = set()
        data_dict = {}

        self.data_dict = data_dict
        self.pair_list = pair_list

    def create_dict(self, l):
        for el_idx, el in enumerate(l):
            if (el not in self.data_dict):
                temp_list = []
                for i_idx, i in enumerate(l):
                    if (i % el == 0) and (el_idx < i_idx):
                        temp_list.append((i,i_idx))
                self.data_dict[(el, el_idx)] = temp_list
        
        # print(self.data_dict)

        

    def add_pair(self, i_all, el_all):
        (i, i_idx) = i_all
        (el, el_idx) = el_all 
        data_tup = ()
        # print('dict',self.data_dict[element_1])
        if self.data_dict[i_all]:
            for element_2 in self.data_dict[i_all]:
                if el_idx<i_idx:
                    data_tup = (el, i, element_2[0])
                    self.pair_list.add(data_tup)

    def get_data(self):
        return ((idx, key, value) for idx, (key, value) in enumerate(self.data_dict.items()))
            
    def check_pairs(self):
        # data_gen = self.get_data()

        for idx, (el_all, value) in enumerate(self.data_dict.items()):
            # print(idx, key, value)
            for i_all in value: 
                self.add_pair(i_all, el_all)     

def solution(l):
    # print(l)
    #duplicate pairs
    #check index values
    #
    if len(l) < 3:
        return 0

    pairs = triplePairs()
    pairs.create_dict(l)
    pairs.check_pairs()
    
    
    return len(pairs.pair_list)

# print(random.sample(range(1, 999999), 2000))

print(solution(random.sample(range(1, 101), 100)))
# print(solution([]))
# print(solution([1,1]))
# print(solution([2,2,2]))