from itertools import combinations

def solution(numbers):
    return sorted(list(set(list(map(sum, combinations(numbers, 2))))))