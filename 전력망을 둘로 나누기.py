from collections import deque, defaultdict


# 1. 선 하나를 제외한다
# 2. 완탐으로 2개로 나눠진 연결 개수를 센다
# 3. 둘을 빼서 최소값 비교한다.

def f(graph, wires, n, excluded_wire):
    start_node = 1
    q = deque([start_node])
    visited = [False] * (n + 1)
    visited[start_node] = 1
    connect_node = 0

    while q:
        now = q.popleft()
        connect_node += 1

        for next in graph[now]:
            if visited[next]: continue
            if [now, next] == excluded_wire or [next, now] == excluded_wire: continue
            visited[next] = 1
            q.append(next)

    other_node = n - connect_node
    return abs(connect_node - other_node)


def solution(n, wires):
    graph = defaultdict(list)
    answer = int(1e9)

    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)

    for excluded_wire in wires:
        res = f(graph, wires, n, excluded_wire)
        answer = min(answer, res)

    return answer
