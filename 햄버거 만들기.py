def solution(ingredient):
    answer = 0
    s = []
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1,2,3,1]:
            answer += 1
            del s[-4:]
    return answer