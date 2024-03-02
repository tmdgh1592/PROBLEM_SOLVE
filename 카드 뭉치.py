from collections import deque


def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for ch in goal:
        if len(cards1) >= 1 and cards1[0] == ch:
            cards1.popleft()
        elif len(cards2) >= 1 and cards2[0] == ch:
            cards2.popleft()
        else:
            return 'No'

    return 'Yes'
