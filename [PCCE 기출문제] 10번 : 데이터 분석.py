columns = {
    "code": 0,
    "date": 1,
    "maximum": 2,
    "remain": 3,
}

def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_i = columns[ext]
    sort_i = columns[sort_by]

    for datum in data:
        if datum[ext_i] < val_ext: answer.append(datum)

    return sorted(answer, key=lambda datum: datum[sort_i])