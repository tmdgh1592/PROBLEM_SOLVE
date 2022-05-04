# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = {id: 0 for id in id_list}
    ban_count = {id: 0 for id in id_list}
    result = {id: [] for id in id_list}

    for now_report in report:
        # id : 유저 ID
        # pid : 유저가 신고한 ID
        id, pid = now_report.split()

        if pid not in result[id]:
            result[id].append(pid)
            ban_count[pid] += 1

    for id, pids in result.items():
        for pid in pids:
            if ban_count[pid] >= k:
                answer[id] += 1

    return list(answer.values())