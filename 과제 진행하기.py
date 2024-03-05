from collections import deque


def parse(time):
    hh, mm = map(int, time.split(':'))
    return hh * 60 + mm


def transform(plans):
    return [(name, parse(start), int(time)) for name, start, time in plans]


def solution(plans):
    plans = deque(sorted(transform(plans), key=lambda x: x[1]))
    answer, pending = [], []
    left_time = 0

    for i in range(len(plans)):
        name, start, time = plans[i]

        while pending:
            _name, work_time = pending.pop()
            if left_time >= work_time:
                left_time -= work_time
                answer.append(_name)
            else:
                pending.append((_name, work_time - left_time))
                break

        pending.append((name, time))

        if i < len(plans) - 1:
            next_start = plans[i + 1][1]
            left_time = next_start - start

    while pending:
        answer.append(pending.pop()[0])

    return answer