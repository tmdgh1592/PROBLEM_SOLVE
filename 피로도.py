answer = -1


def solution(k, dungeons):
    visited = [False] * len(dungeons)

    def f(cnt, peero):
        global answer

        if sum(visited) == len(dungeons):
            answer = max(answer, cnt)
            return

        for i in range(len(dungeons)):
            if visited[i]: continue
            visited[i] = True
            if peero >= dungeons[i][0]:
                f(cnt + 1, peero - dungeons[i][1])
            else:
                f(cnt, peero)
            visited[i] = False

    f(0, k)
    return answer