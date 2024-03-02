def solution(s):
    answer = 0
    start_ch = s[0]

    same_count = 0
    diff_count = 0

    for i, ch in enumerate(s):
        if ch == start_ch:
            same_count += 1
        else:
            diff_count += 1

        if same_count == diff_count:
            answer += 1
            same_count = 0
            diff_count = 0
            if i + 1 < len(s):
                start_ch = s[i + 1]

    if same_count != diff_count:
        answer += 1

    return answer