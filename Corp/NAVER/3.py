# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from typing import Dict


def solution(A, B, C):
    answer = ''

    # 셋 중에 하나만 0이 아닌 경우
    if A == 0 and B == 0 and C != 0:
        return 'c' * min(2, C)
    elif A == 0 and B != 0 and C == 0:
        return 'b' * min(2, B)
    elif A != 0 and B == 0 and C == 0:
        return 'a' * min(2, A)

    # 여기서부터는 최소한 2개 이상이 0보다 큼
    alpha_dict = {'a': A, 'b': B, 'c': C}
    copy_alpha_dict = alpha_dict.copy()

    used = max_three_alpha(alpha_dict['a'], alpha_dict['b'], alpha_dict['c'])
    answer += used * min(2, alpha_dict[used])
    alpha_dict[used] -= min(2, alpha_dict[used])

    copy_alpha_dict.pop(used)
    next_use = max_two_alpha(copy_alpha_dict)  # 다음에 쓸 알파벳

    while used != next_use and next_use != 'x':
        cnt = min(alpha_dict[next_use], 2)
        answer += next_use * cnt
        alpha_dict[next_use] -= cnt

        used = next_use

        copy_alpha_dict = alpha_dict.copy()
        copy_alpha_dict.pop(used)

        next_use = max_two_alpha(copy_alpha_dict)

    return answer


def max_three_alpha(A, B, C):
    dic = {0: 'a', 1: 'b', 2: 'c'}
    arr = [A, B, C]
    max_val = max(A, B, C)
    return dic[arr.index(max_val)]


def max_two_alpha(alpha_dict: Dict):
    if sum(list(alpha_dict.values())) == 0:
        return 'x'

    arr = list(alpha_dict.values())  # 남은 알파벳 개수 리스트
    return list(alpha_dict.keys())[arr.index(max(arr))]