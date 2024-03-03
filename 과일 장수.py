def solution(k, m, score):
    answer = 0

    score = sorted(score, reverse=True)
    box = []

    for i in range(len(score)):
        box.append(score[i])
        if (i + 1) % m == 0:
            answer += min(box) * m
            box.clear()

    return answer
