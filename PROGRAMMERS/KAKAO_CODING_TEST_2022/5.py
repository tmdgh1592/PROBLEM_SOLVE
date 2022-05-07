# 효율성 실패

def solution(rc, operations):
    for op in operations:
        if op == "ShiftRow":
            prev_temp = rc[0]
            now_temp = rc[0]
            for i in range(1, len(rc)):
                now_temp = rc[i]
                rc[i] = prev_temp
                prev_temp = now_temp
                if i == len(rc)-1:
                    rc[0] = prev_temp
        else:
            garo, sero = len(rc[0]), len(rc)
            # ran = (garo*sero) - ((garo-1)*(sero-1))  # 반복할 횟수
            prev_temp = rc[0][0]
            now_temp = rc[0][0]
            i, j = 0, 1
            direction = 0

            while direction != 4:
                now_temp = rc[i][j]
                rc[i][j] = prev_temp
                prev_temp = now_temp
                if direction == 0:
                    j += 1
                elif direction == 1:
                    i += 1
                elif direction == 2:
                    j -= 1
                else:
                    i -= 1

                if j == garo:
                    j -= 1
                    i += 1
                    direction += 1
                elif i == sero:
                    i -= 1
                    j -= 1
                    direction += 1
                elif j == -1:
                    j = 0
                    i = sero - 2
                    direction += 1
                elif i == -1:
                    direction += 1
                    break

    return rc
