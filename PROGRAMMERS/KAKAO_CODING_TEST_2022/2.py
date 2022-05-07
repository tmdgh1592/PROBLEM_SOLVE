# 부분 성공

from collections import deque


def solution(queue1: list, queue2: list):
    answer = 0
    org_q1 = deque(queue1)
    org_q2 = deque(queue2)

    if (sum(queue1) == sum(queue2)):
        return answer
    

    q_len = len(queue1)

    for i in range(q_len):
        q1 = org_q1.copy()
        q2 = org_q2.copy()
        answer = 0

        for _ in range(i+1):
            q1.append(q2.popleft())
            answer += 1
        if sum(q1) == sum(q2):
            print(q1, q2)
            return answer

        q1_len = len(q1)
        for j in range(q1_len-1):
            q2.append(q1.popleft())
            answer += 1
            if sum(q1) == sum(q2):
                print(q1, q2)
                return answer

    return -1


print(solution([1000000000, 3], [1, 1000000000]))
