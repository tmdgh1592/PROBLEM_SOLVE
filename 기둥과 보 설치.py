def solution(n, build_frame):
    answer = set()

    def satisfy():
        for x, y, a in answer:
            if a == 0:
                if not (y == 0 or (x - 1, y, 1) in answer or (x, y - 1, 0) in answer or (x, y, 1) in answer):
                    return False
            if a == 1:
                if not ((x, y - 1, 0) in answer or (x + 1, y - 1, 0) in answer or (
                        (x - 1, y, 1) in answer and (x + 1, y, 1) in answer)):
                    return False

        return True

    for x, y, a, b in build_frame:
        if b == 0:
            answer.remove((x, y, a))
            if not satisfy():
                answer.add((x, y, a))

        if b == 1:
            answer.add((x, y, a))
            if not satisfy():
                answer.remove((x, y, a))

    return sorted(answer)
