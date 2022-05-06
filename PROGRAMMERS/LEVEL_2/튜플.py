def solution(s: str):
    answer = []
    answer_set = set()
    my_sets = str_to_set(s)

    for my_set in my_sets:
        answer.append((my_set - answer_set).pop())
        answer_set = my_set

    return answer


def str_to_set(s: str):
    strings = s[1:-1].replace("{", '')[:-1].split("},")
    my_set = []

    for string in strings:
        my_set.append(set(map(int, string.split(','))))

    return sorted(my_set, key=len)
