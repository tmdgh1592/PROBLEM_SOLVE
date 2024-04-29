answers = {}  # 이번달 선물 예측
gift_points = {}  # 선물 지수
send = {}  # A가 B에게 선물한 횟수 기록
treated = {}


def init_data(friends):
    for a in friends:
        answers[a] = 0
        gift_points[a] = 0
        for b in friends:
            if a == b: continue
            send[(a, b)] = 0
            send[(b, a)] = 0
            treated[(a, b)] = False
            treated[(b, a)] = False


def solution(friends, gifts):
    init_data(friends)

    for gift in gifts:  # 선물 지수 구하기
        a, b = gift.split()
        gift_points[a] += 1
        gift_points[b] -= 1
        send[(a, b)] += 1

    for a in friends:
        for b in friends:
            if a == b: continue
            if treated[(a, b)]: continue
            if treated[(b, a)]: continue
            treated[(a, b)] = True
            treated[(b, a)] = True
            if send[(a, b)] > send[(b, a)]:
                answers[a] += 1
            elif send[(a, b)] < send[(b, a)]:
                answers[b] += 1
            else:
                if gift_points[a] > gift_points[b]:
                    answers[a] += 1
                elif gift_points[a] < gift_points[b]:
                    answers[b] += 1

    print(answers)
    return max(answers.values())
