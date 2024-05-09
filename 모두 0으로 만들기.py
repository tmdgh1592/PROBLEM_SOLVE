import sys

sys.setrecursionlimit(int(1e6))


def solution(costs, edges):
    if sum(costs) != 0: return -1
    n = len(costs)

    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def f(now, parent):
        result = 0
        for child in graph[now]:
            if child != parent:
                result += f(child, now)

        result += abs(costs[now])
        costs[parent] += costs[now]
        return result

    return f(0, 0)