def solution(t, p):
    i = 0
    j = len(p) - 1
    answer = 0

    while j < len(t):
        if int(t[i : j+1]) <= int(p):
            answer += 1

        i += 1
        j += 1

    return answer