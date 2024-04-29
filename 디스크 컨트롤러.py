import heapq


def solution(jobs):
    s, e, i = -1, 0, 0
    answer = 0
    q = []

    while i < len(jobs):
        for job in jobs:
            if s < job[0] <= e:
                heapq.heappush(q, [job[1], job[0]])

        if q:
            duration, request_time = heapq.heappop(q)
            s = e
            e += duration
            answer += e - request_time
            i += 1
        else:
            e += 1
    return answer // len(jobs)