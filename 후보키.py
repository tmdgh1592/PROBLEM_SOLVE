from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    comb = []
    for i in range(1, col + 1):
        comb.extend(list(combinations(range(col), i)))

    unique = []
    for rows in comb:
        tmp = [tuple(data[key] for key in rows) for data in relation]
        if len(set(tmp)) == len(tmp):
            unique.append(rows)

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    return len(answer)