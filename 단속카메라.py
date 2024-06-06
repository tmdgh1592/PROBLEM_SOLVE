def solution(routes):
    routes.sort(key=lambda x: x[1])

    answer = 1
    end = routes[0][1]

    for s, e in routes[1:]:
        if not (s <= end <= e):
            end = e
            answer += 1

    return answer
