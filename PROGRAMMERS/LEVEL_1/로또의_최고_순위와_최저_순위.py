def solution(lottos, win_nums):
    answer = [0, 0]
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    count = 0
    for x in lottos:
        for y in win_nums:
            if x == y:
                count += 1
                break
    answer[1] = rank[count]

    for x in lottos:
        if x == 0:
            count += 1
    answer[0] = rank[count]

    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
