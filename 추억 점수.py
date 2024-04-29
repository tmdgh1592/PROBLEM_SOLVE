def solution(name, yearning, photo):
    answer = []
    miss_scores = {name[i] : yearning[i] for i in range(len(name))}

    for people in photo:
        score = 0
        for person in people:
            if person not in miss_scores: continue
            score += miss_scores[person]
        answer.append(score)

    return answer