import heapq

def solution(k, score):
    answer = []
    q = []
    n = len(score)

    for i in range(1, n + 1):
        heapq.heappush(q, score[i - 1])
        if i > k: heapq.heappop(q)
        answer.append(q[0])

    return answer
