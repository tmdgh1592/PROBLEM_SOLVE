from itertools import permutations


def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(x ** (1 / 2)) + 1):
        if x % i == 0: return False
    return True


def solution(numbers):
    numbers = list(map(int, list(numbers)))
    prime_set = set()

    for i in range(1, len(numbers) + 1):
        pers = permutations(numbers, i)
        for per in pers:
            num = 0
            for j in range(len(per) - 1, -1, -1):
                num += per[j] * 10 ** j

            if is_prime(num):
                prime_set.add(num)

    return len(prime_set)