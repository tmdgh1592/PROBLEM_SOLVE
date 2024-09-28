def solution(targets):
    cur = -1
    cnt = 0
    targets.sort(key=lambda x:x[1])
    
    for s, e in targets:
        if s >= cur:
            cur = e
            cnt += 1
    
    return cnt