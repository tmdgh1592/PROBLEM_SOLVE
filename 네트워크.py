from collections import deque


def solution(n, computers):
    def f(start):
        q = deque([start])
        while q:
            now = q.popleft()
            computers[now][now] = 0

            for i, can_go_next in enumerate(computers[now]):
                if not can_go_next: continue
                computers[now][i] = 0
                computers[i][now] = 0
                q.append(i)

    answer = 0
    for i in range(n):
        if computers[i][i] != 0:
            f(i)
            answer += 1

    return answer
