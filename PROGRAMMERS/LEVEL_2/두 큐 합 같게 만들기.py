from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1); queue2 = deque(queue2)
    a_sum = sum(queue1); b_sum = sum(queue2)
    a_len = len(queue1); b_len = len(queue2)
    
    if (a_sum + b_sum) % 2 != 0:
        return -1
    
    while answer < 2 * (a_len + b_len):
        if a_sum > b_sum:
            num = queue1.popleft()
            queue2.append(num)
            a_sum -= num; b_sum += num
        elif a_sum < b_sum:
            num = queue2.popleft()
            queue1.append(num)
            b_sum -= num; a_sum += num
        else: break
        answer += 1
    
    return answer if a_sum == b_sum else -1