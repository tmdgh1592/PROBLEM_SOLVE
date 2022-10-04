def solution(survey, choices):
    score = [0, 3, 2, 1, 0 ,1, 2, 3]
    mdict = {'R': 0, 'T': 0,'C': 0,'F': 0,'J': 0,'M': 0,'A': 0,'N': 0}
    
    for i in range(len(choices)):
        type_a, type_b = list(survey[i])
        if choices[i] >= 4:
            mdict[type_a] += score[choices[i]]
        else:
            mdict[type_b] += score[choices[i]]
    
    answer = ""
    result = list(mdict.items())
    i = 0
    while i < 8:
        if result[i][1] < result[i+1][1]:
            answer += result[i][0]
        elif result[i][1] > result[i+1][1]:
            answer += result[i+1][0]
        else:
            if ord(result[i][0]) < ord(result[i+1][0]):
                answer += result[i][0]
            else:
                answer += result[i+1][0]
        i += 2

    return answer