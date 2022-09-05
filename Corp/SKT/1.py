def solution(p):
    answer = [0 for _ in range(len(p))]
    for i in range(len(p)):
        min_idx = i
        for j in range(i+1, len(p)):
            if p[min_idx] > p[j]:
                min_idx = j

        if min_idx != i:
            p[i], p[min_idx] = p[min_idx], p[i]  # swap
            answer[i] += 1
            answer[min_idx] += 1

    return answer


print(solution([2, 5, 3, 1, 4]))
