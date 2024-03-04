def solution(a, b, n):
    answer = 0
    empty = n

    while empty >= a:
        new_coke = b * (empty // a)  # 빈병 a개당 b개 획득
        answer += new_coke
        empty = new_coke + empty % a  # 새로운 coke를 다 마시고, 교환하고 남은 병을 다시 합해줌

    return answer
