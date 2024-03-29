mdict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def parse(num, n):
    if num == 0: return '0'

    val = ''
    while num > 0:
        num, mod = divmod(num, n)
        if mod >= 10: mod = mdict[mod]
        val += str(mod)

    return val[::-1]


def solution(n, t, m, p):
    mstr = ''
    answer = ''
    num = p - 1
    for num in range(t * m):
        mstr += parse(num, n)

    i = p - 1
    while len(answer) < t:
        answer += mstr[i]
        i += m

    return answer