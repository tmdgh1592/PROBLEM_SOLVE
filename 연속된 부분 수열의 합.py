def solution(sequence, k):
    answer = []
    interval_sum, e = 0, 0
    interval_sum = 0

    for s in range(len(sequence)):
        while interval_sum < k and e < len(sequence):
            interval_sum += sequence[e]
            e += 1

        if interval_sum == k:
            if len(answer) == 0:
                answer = [s, e - 1]
            else:
                asum = answer[1] - answer[0]
                bsum = e - 1 - s
                if bsum < asum:
                    answer = [s, e - 1]
        interval_sum -= sequence[s]

    return answer