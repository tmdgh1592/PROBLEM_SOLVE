from collections import deque


def solution(priorities, location):
    orders = sorted(priorities)
    priorities = deque([(i, priority) for i, priority in enumerate(priorities)])
    order = 0

    while priorities:
        max_num = orders[-1]
        loc, num = priorities.popleft()

        if num == max_num:
            order += 1
            orders.pop()
            if loc == location:
                return order

        if num != max_num:
            priorities.append((loc, num))
