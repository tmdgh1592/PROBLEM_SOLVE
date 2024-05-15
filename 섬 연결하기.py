def solution(n, costs):
    def find_parent(x):
        if x != parent[x]:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union_parent(a, b):
        a = find_parent(a)
        b = find_parent(b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    for a, b, cost in costs:
        if find_parent(a) != find_parent(b):
            answer += cost
            union_parent(a, b)

    return answer
