answer = []
max_diff = int(1e9)


def calc(a_list, b_list):
    a_score, b_score = 0, 0

    for i in range(11):
        a, b = a_list[i], b_list[i]
        if a == 0 and b == 0: continue
        elif a >= b: a_score += (10 - i)
        else: b_score += (10 - i)

    return a_score - b_score

def solution(n, info):
    def compare(lion):
        global answer, max_diff
        diff = calc(info, lion)

        if diff < 0:
            if not sum(answer):
                max_diff = diff
                return lion
            if max_diff > diff:
                max_diff = diff
                return lion
            if max_diff == diff:
                for i in range(10, -1, -1):
                    if lion[i] > answer[i]:
                        return lion
                    elif lion[i] < answer[i]:
                        return answer
        return answer

    def f(lion, win_info, i):
        global answer

        if i == 11:
            answer = compare(lion)
            return

        if i == 10:
            remain_arrow = n - sum(lion)
            lion[i] = remain_arrow
        elif win_info[i] == '1':
            win_lion_score = info[i] + 1
            remain_arrow = n - sum(lion)
            if remain_arrow >= win_lion_score:
                lion[i] = win_lion_score

        f(lion, win_info, i + 1)

    for i in range(1 << 11):
        win_info = (bin(i)[2:]).zfill(11)
        f([0] * 11, win_info, 0)

    return [-1] if (sum(answer) == 0) else answer