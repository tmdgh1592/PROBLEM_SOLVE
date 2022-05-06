INF = int(1e9)

def solution(stones, k):
    answer = 0
    while True:
        for i in range(len(stones)):
            if stones[i] <= 0:  # 현재 건너려는 다리가 못건너는 경우라면
                # add_i는 몇 칸 건넌지 인덱스
                # success는 건너기에 성공했는지 여부
                # 범위 내의 다음 다리들은 건널 수 있는지 체크
                add_i, success = check(stones, i, k)
                if success:
                    i += add_i
                elif success and add_i == INF:
                    return answer + 1
                else:
                    return answer

        stones = list(map(lambda x: x-1, stones))
        answer += 1


def check(stones: list, now_pos, k):
    for i in range(1, k):
        if now_pos+i >= len(stones):  # 징검다리를 완전히 넘어간 경우
            return (INF, True)
        if stones[now_pos+i] > 0:  # i ~ k 번째 사이의 돌들이 건널 수 있는 상태라면
            return (i, True)

    return 0, False
