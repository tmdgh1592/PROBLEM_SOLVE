def solution(n, t, m, timetable):
    timetable = sorted([60 * int(time[:2]) + int(time[3:]) for time in timetable])
    bustime = [9 * 60 + t * i for i in range(n)]

    idx = 0
    for bus in bustime:
        cnt = 0
        while cnt < m and idx < len(timetable) and timetable[idx] <= bus:
            cnt += 1
            idx += 1
        if cnt < m:
            answer = bus
        else:
            answer = timetable[idx - 1] - 1

    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)
