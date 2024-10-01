def solution(cap, n, deliveries, pickups):
    answer = 0
    must_deli, must_pick = 0, 0
    
    for i in range(n - 1, -1, -1):
        must_deli += deliveries[i]
        must_pick += pickups[i]
        
        while must_deli > 0 or must_pick > 0:
            answer += (i + 1) * 2
            must_deli -= cap
            must_pick -= cap
    
    return answer
