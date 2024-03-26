def solution(name):
    answer = 0

    lr_move = len(name) - 1

    for i, ch in enumerate(name):
        answer += min(ord(ch) - ord('A'), ord('Z') + 1 - ord(ch))

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        lr_move = min([lr_move, 2 * i + len(name) - next, 2 * (len(name) - next) + i])

    return answer + lr_move