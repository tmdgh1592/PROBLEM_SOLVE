# 정답

def solution(survies: list, choices: list):
    answer = ''
    score = [0, -3, -2, -1, 0, 1, 2, 3]
    result_dict = {'R': 0, 'T': 0, 'C': 0,
                   'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(len(survies)):
        result_dict[survies[i][1]] += score[choices[i]]

    keys = list(result_dict.keys())
    for i in range(0, 8, 2):
        if result_dict[keys[i]] >= result_dict[keys[i+1]]:
            answer += keys[i]
        else:
            answer += keys[i+1]

    return answer
