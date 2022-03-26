from collections import deque
import sys
input = sys.stdin.readline


def topology(dest):
    max_cost = [0] * (v+1)  # 최대 비용 리스트
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
            max_cost[i] = cost[i]  # 최초 시작지점 비용 설정

    while q:
        now = q.popleft()
        for i in graph[now]:
            # 진입차수가 0이면 다음 작업을 위해 q에 추가
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

            # 현재까지의 비용과 다음 노드의 비용의 합 최대 갱신
            c = cost[i] + max_cost[now]
            max_cost[i] = max(max_cost[i], c)

    # print(max_cost)
    return max_cost[dest]


T = int(input())

for _ in range(T):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    indegree = [0] * (v+1)
    cost = [0] + list(map(int, input().split()))

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    dest = int(input())

    print(topology(dest))
