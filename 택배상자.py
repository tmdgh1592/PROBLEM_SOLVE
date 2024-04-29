from collections import deque


def solution(order):
    answer = 0
    container = deque([i + 1 for i in range(len(order))])
    sub_container = []

    for item in order:
        can = False
        if sub_container and sub_container[-1] == item:
            sub_container.pop()
            answer += 1
            continue

        while container:
            can = True
            if container[0] == item:
                container.popleft()
                answer += 1
                break
            sub_container.append(container.popleft())

        if not can: break
    return answer
