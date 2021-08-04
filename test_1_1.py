'''
1-1
RE-ID
Find the RE-ID string from a long string of prime numbers
'''
def is_prime(num):
    for idx in range(2, int(num/2)+1):
        if (num % idx) == 0:
            return False
    else:
        return True
    
def solution(i):
    num = 2
    prime_string = ""

    while len(prime_string) < (i+5):
        if is_prime(num):
            prime_string = prime_string + str(num)
        num+=1
    return prime_string[i: i+5]
    

'''
Test cases
'''
import pytest
def test_pass_1():
    assert solution(0) == "23571"

def test_pass_2():
    assert solution(5000) == "05131"
    
def test_pass_3():
    assert solution(3) == "71113"

def test_fail_1():
    with pytest.raises(TypeError):
        solution()