def solution(picks, minerals):
    answer = float('inf')

    def f(cur_pick, remain_minerals, score):
        nonlocal answer
        now_score = score

        if cur_pick == 0:
            for mineral in remain_minerals[:5]:
                now_score += 1
        if cur_pick == 1:
            for mineral in remain_minerals[:5]:
                if mineral == 'diamond':
                    now_score += 5
                else:
                    now_score += 1
        if cur_pick == 2:
            for mineral in remain_minerals[:5]:
                if mineral == 'diamond':
                    now_score += 25
                elif mineral == 'iron':
                    now_score += 5
                else:
                    now_score += 1

        if not remain_minerals[5:] or sum(picks) == 0:
            answer = min(answer, now_score)
            return

        for tool, tool_cnt in enumerate(picks):
            if tool_cnt > 0:
                picks[tool] -= 1
                f(tool, remain_minerals[5:], now_score)
                picks[tool] += 1

    for tool, tool_cnt in enumerate(picks):
        if tool_cnt > 0:
            picks[tool] -= 1
            f(tool, minerals, 0)
            picks[tool] += 1

    return answer
