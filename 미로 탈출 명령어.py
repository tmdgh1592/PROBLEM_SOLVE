import math


def check(bin_num):
    if len(bin_num) == 1: return True

    root = len(bin_num) // 2
    if bin_num[root] == '0':
        return '1' not in bin_num

    return check(bin_num[:root]) and check(bin_num[root + 1:])


def solution(numbers):
    answer = []

    for num in numbers:
        num = bin(num)[2:]
        digit = 2 ** (int(math.log(len(num), 2)) + 1) - 1
        num = "0" * (digit - len(num)) + num

        answer.append(1 if check(num) else 0)

    return answer