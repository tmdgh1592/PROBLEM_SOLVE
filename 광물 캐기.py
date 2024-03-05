from collections import deque
import copy

answer = int(1e9)


def f(picks, minerals, tired):
    global answer

    if sum(picks) == 0 or not minerals:
        answer = min(answer, tired)
        return

    for i in range(3):
        if picks[i] == 0: continue

        picks[i] -= 1
        added_tired = 0
        copied_minerals = copy.deepcopy(minerals)

        for _ in range(5):
            if not copied_minerals: break

            mineral = copied_minerals.popleft()
            if i == 0:
                added_tired += 1
            elif i == 1 and mineral == "diamond":
                added_tired += 5
            elif i == 1:
                added_tired += 1
            elif i == 2 and mineral == "diamond":
                added_tired += 25
            elif i == 2 and mineral == "iron":
                added_tired += 5
            else:
                added_tired += 1

        f(picks, copied_minerals, tired + added_tired)
        picks[i] += 1


def solution(picks, minerals):
    f(picks, deque(minerals), 0)
    return answer
