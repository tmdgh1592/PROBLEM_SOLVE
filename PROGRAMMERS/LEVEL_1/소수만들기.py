from itertools import combinations
from math import sqrt

def isprime(num):
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    combs = combinations(nums, 3)
    for comb in combs:
        if isprime(sum(comb)):
            print(comb)
            answer += 1
        
    return answer