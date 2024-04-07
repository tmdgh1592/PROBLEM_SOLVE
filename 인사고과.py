def solution(scores):
    answer = 1
    whanho = scores[0]
    maximum = -1
    
    scores.sort(key=lambda x:(-x[0], x[1]))
    for x, y in scores:
        wx, wy = whanho
        if wx < x and wy < y: return -1
        if sum(whanho) < sum([x,y]) and y >= maximum:
            maximum = y
            answer += 1
        
    return answer