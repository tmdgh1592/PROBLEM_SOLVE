def solution(storey):
    answer = 0

    while storey:
        remain = storey % 10
        if remain > 5:
            answer += 10 - remain
            storey += 10 - remain
        elif remain < 5:
            answer += remain
        else:
            if (storey // 10) % 10 >= 5:
                storey += 5
            answer += 5
        storey //= 10

    return answer