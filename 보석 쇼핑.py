from collections import defaultdict


def solution(gems):
    gem_type_cnt = len(set(gems))
    n = len(gems)

    has_gems = defaultdict(int)
    answer = [0, int(1e9)]

    e = 0
    for s in range(n):
        while e < n and len(has_gems) != gem_type_cnt:
            has_gems[gems[e]] += 1
            e += 1

        if len(has_gems) == gem_type_cnt:
            if e - 1 - s < answer[1] - answer[0]:
                answer = [s + 1, e]

        has_gems[gems[s]] -= 1
        if has_gems[gems[s]] == 0:
            del has_gems[gems[s]]

    return answer