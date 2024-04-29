import heapq


def solution(info, edges):
    visited = [False] * len(info)
    answer = []

    def f(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c]:
                    f(sheep, wolf + 1)
                else:
                    f(sheep + 1, wolf)
                visited[c] = False

    visited[0] = 1
    f(1, 0)
    return max(answer)