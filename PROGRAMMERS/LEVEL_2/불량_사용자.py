from itertools import permutations


def solution(user_id: list, banned_id: list):
    result = []

    pair_id_list = list(permutations(user_id, len(banned_id)))  # if len == 2

    for pair_ids in pair_id_list:
        if check(pair_ids, banned_id):  # pair_ids = [frodo, fradi]
            if set(pair_ids) not in result:
                result.append(set(pair_ids))

    return len(result)


def check(pair_user_id: list, banned_id: list):
    for i in range(len(banned_id)):
        if len(pair_user_id[i]) != len(banned_id[i]):
            return False

        user_id = pair_user_id[i]
        ban_id = banned_id[i]

        for idx in range(len(user_id)):
            if ban_id[idx] != '*':
                if ban_id[idx] != user_id[idx]:
                    return False
    return True
