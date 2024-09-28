def parse(time):
    h, m = map(int, time.split(":"))
    return 60 * h + m

def solution(plans):
    plans = sorted([(name, parse(start), int(work)) for name, start, work in plans], key=lambda x:x[1])
    answer, pending = [], []
    left_time = 0
    
    for i, (name, start, time) in enumerate(plans):
        while pending:
            _name, remain_time = pending.pop()
            if left_time >= remain_time:
                left_time -= remain_time
                answer.append(_name)
            else:
                pending.append((_name, remain_time - left_time))
                break
        
        pending.append((name, time))

        if i < len(plans) - 1:
            left_time = plans[i+1][1] - start
        
    while pending:
        answer.append(pending.pop()[0])
    
    return answer
    