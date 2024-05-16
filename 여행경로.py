from collections import defaultdict, deque
import sys

sys.setrecursionlimit(int(1e6))


def solution(tickets):
    answer = []
    graph = defaultdict(list)
    visited = defaultdict(bool)
    n = len(tickets)

    for id, (a, b) in enumerate(tickets):
        graph[a].append((id, b))

    paths = []

    def f(now, path):
        if len(path) == n + 1:
            paths.append(path)
            return

        for id, next in graph[now]:
            if visited[id]: continue
            visited[id] = True
            f(next, path[:] + [next])
            visited[id] = False

    f("ICN", ["ICN"])
    return sorted(paths)[0]
