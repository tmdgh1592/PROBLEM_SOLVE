def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    x, y, num = 0, -1, 1

    for i in range(n):
        for j in range(n - i):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            answer[y][x] = num
            num += 1

    return sum(answer, [])