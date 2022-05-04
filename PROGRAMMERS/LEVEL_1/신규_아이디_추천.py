# https://programmers.co.kr/learn/courses/30/lessons/72410
import re


def solution(new_id):
    # 1단계
    new_id = str(new_id).lower()

    # 2단계
    new_id_list = [c for c in new_id if c.isalnum()
                   or c == '-' or c == '_' or c == '.']

    # 4단계
    while len(new_id_list) >= 1 and new_id_list[0] == '.':
        new_id_list.pop(0)
    while len(new_id_list) >= 1 and new_id_list[len(new_id_list)-1] == '.':
        new_id_list.pop(len(new_id_list)-1)

    # 3단계
    i = 0
    while i < len(new_id_list)-1:
        if new_id_list[i] == '.' and new_id_list[i+1] == '.':
            new_id_list.pop(i+1)
        else:
            i += 1

    # 5단계
    if len(new_id_list) == 0:
        new_id_list.append('a')

    # 6단계
    if len(new_id_list) >= 16:
        new_id_list = new_id_list[:15]
        if new_id_list[len(new_id_list)-1] == '.':
            new_id_list.pop(len(new_id_list)-1)

    # 7단계
    if len(new_id_list) <= 2:
        new_id_list += [new_id_list[-1]] * (3 - len(new_id_list))

    return ''.join(new_id_list)
