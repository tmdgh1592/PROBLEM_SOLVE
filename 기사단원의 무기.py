def yaksoo(num):
    cnt = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0: cnt += 1
    cnt *= 2

    return cnt - 1 if int(num ** 0.5) ** 2 == num else cnt

def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        yaksoo_cnt = yaksoo(i)
        answer += power if yaksoo_cnt > limit else yaksoo_cnt
    return answer