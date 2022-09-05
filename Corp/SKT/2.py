# periods : 고객들 가입기간
# payments : 고객들의 납부 이전 내역
# estimates : 고객들의 납부 예정 금액

# VIP 기준 : (연간 납부 금액 90만원 이상) and (가입 2년 이상)
# VIP 기준 : (연간 납부 금액 60만원 이상) ~ 90만원 미만 and (가입 5년 이상)

def solution(periods, payments, estimates):
    answer = [0, 0]

    for i in range(len(periods)):
        payment = payments[i]  # 월간 납부금액 리스트
        now_year_payment = sum(payment)  # 연간 납부 금액
        next_year_payment = sum(payment[1:]) + estimates[i]
        now_period = periods[i]
        next_period = periods[i] + 1

        if now_year_payment >= 900000 and now_period >= 24:  # 이번달에 VIP
            if next_year_payment < 900000: # 다음달에 VIP 아님
                answer[1] += 1
        elif 600000 <= now_year_payment < 900000 and now_period >= 60:  # 이번달에 VIP
            if next_year_payment < 600000: # 다음달에 VIP 아님
                answer[1] += 1
        else: # 이번달에 VIP 아님!
            if (next_year_payment >= 900000 and next_period >= 24) or (600000 <= next_year_payment < 900000 and next_period >= 60):  # 다음 달에 VIP
                answer[0] += 1
            

    return answer
