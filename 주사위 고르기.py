from collections import defaultdict
from bisect import bisect_left, bisect_right

# 1. 주사위 n개를 반으로 나눈 모든 경우의 수를 돌린다.
# 2. n/2개가 모였을 때 승리하는 경우의 수를 구한다.
# 3. 크면 answer 업데이트
# !! 1,2의 승리는 3,4의 패배 (= 반대와 동일) -> 1,2구했으면 3,4 계산할 필요X
# 1,2의 승리 계산하면 3,4의 패배가 곧 3,4의 승리

answer = []
visited = defaultdict(bool)
other_dfs_result = []
win, lose, max_win = 0, 0, -1


def solution(dice):
    n = len(dice)

    def other_dfs(i, others, numbers, score):
        global win, lose

        if len(numbers) == n // 2:
            other_sum = sum(numbers)
            other_dfs_result.append(other_sum)
            if score > other_sum:
                win += 1
            elif score < other_sum:
                lose += 1
            return

        for x in dice[others[i]]:
            numbers.append(x)
            other_dfs(i + 1, others, numbers, score)
            numbers.pop()

    def dfs(i, dices, others, numbers):
        global win, lose, other_dfs_result

        if len(numbers) == n // 2:
            my_sum = sum(numbers)
            # 상대 경우의 숫자 모집해서 계산하기
            if other_dfs_result:
                win += bisect_left(other_dfs_result, my_sum)
                lose += len(other_dfs_result) - bisect_right(other_dfs_result, my_sum)
            else:
                other_dfs(0, others, [], my_sum)
                other_dfs_result = sorted(other_dfs_result)
            return

        for x in dice[dices[i]]:
            numbers.append(x)
            dfs(i + 1, dices, others, numbers)
            numbers.pop()

    def calc(dices):
        global answer, win, lose, max_win, other_dfs_result
        win, lose = 0, 0
        visited[str(dices)] = True
        dices_set = set(dices)
        others = []
        other_dfs_result = []

        for i in range(n):
            if i not in dices_set:
                others.append(i)
        visited[str(others)] = True
        dfs(0, dices, others, [])

        if max_win < win:
            max_win = win
            answer = dices[:]

        if max_win < lose:
            max_win = lose
            answer = others[:]

    def f(start, dices):
        if len(dices) == n // 2:
            if visited[str(dices)]: return
            calc(dices)
            return

        for i in range(start, n):
            dices.append(i)
            f(i + 1, dices)
            dices.pop()

    f(0, [])
    return [i + 1 for i in answer]