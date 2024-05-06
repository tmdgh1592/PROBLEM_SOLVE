def str_to_int(time):
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s


def int_to_str(time):
    h = time // 3600
    time %= 3600
    m = time // 60
    s = time % 60

    h = '0' + str(h) if h < 10 else h
    m = '0' + str(m) if m < 10 else m
    s = '0' + str(s) if s < 10 else s
    return f'{h}:{m}:{s}'


def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    viewers = [0 for _ in range(play_time + 1)]

    logs = [list(map(str_to_int, l.split("-"))) for l in logs]

    for s, e in logs:
        viewers[s] += 1
        viewers[e] -= 1

    for i in range(1, play_time):
        viewers[i] += viewers[i - 1]

    for i in range(1, play_time):
        viewers[i] += viewers[i - 1]

    max_view = 0
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if viewers[i] - viewers[i - adv_time] > max_view:
            max_view = viewers[i] - viewers[i - adv_time]
            max_time = i - adv_time + 1

    return int_to_str(max_time)