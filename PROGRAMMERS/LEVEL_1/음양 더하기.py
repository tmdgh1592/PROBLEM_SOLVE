def solution(absolutes, signs):
    answer = 0
    sign = {True : 1, False : -1}
    for i in range(len(absolutes)):
        answer += (absolutes[i] * sign[signs[i]])
    
    return answer