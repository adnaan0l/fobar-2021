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
    
print(solution(0))
print(solution(5000))
print(solution(3))