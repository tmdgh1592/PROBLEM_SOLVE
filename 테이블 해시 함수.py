def sort(data, col):
    return sorted(data, key=lambda x: (x[col], -x[0]))


def mod(data, val):
    res = 0
    for x in data:
        res += x % val
    return res


def solution(data, col, row_begin, row_end):
    data = sort(data, col - 1)
    row_begin -= 1
    answer = 0
    for i in range(row_begin, row_end):
        val = mod(data[i], i + 1)
        answer ^= val

    return answer