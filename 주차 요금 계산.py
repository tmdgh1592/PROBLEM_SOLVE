from math import ceil
from collections import defaultdict


def parse(time):
    hh, mm = map(int, time.split(':'))
    return hh * 60 + mm


def solution(fees, records):
    answer = []
    times = defaultdict(int)  # 0000 : 345
    in_outs = {}  # 0000 : 320

    for record in records:
        time, car, in_out = record.split()
        time = parse(time)

        if in_out == "IN":
            in_outs[car] = time
        elif in_out == "OUT":
            times[car] += time - in_outs[car]
            del in_outs[car]

    for car, in_time in in_outs.items():
        times[car] += parse('23:59') - in_time

    infos = sorted(times.items())
    for car, time in infos:
        if time <= fees[0]:
            answer.append(fees[1])
        elif time > fees[0]:
            answer.append(fees[1] + ceil((time - fees[0]) / fees[2]) * fees[3])

    return answer
