from collections import defaultdict
import heapq


def solution(genres, plays):
    answer = []
    genre_scores = defaultdict(int)
    mgenres = defaultdict(list)

    for i in range(len(genres)):
        genre_scores[genres[i]] += plays[i]
    genre_scores = dict(sorted(genre_scores.items(), key=lambda x: -x[1]))

    for id in range(len(genres)):
        heapq.heappush(mgenres[genres[id]], (-plays[id], id))

    for genre in genre_scores.keys():
        cnt = len(mgenres[genre])
        for i in range(min(cnt, 2)):
            score, id = heapq.heappop(mgenres[genre])
            answer.append(id)

    return answer
