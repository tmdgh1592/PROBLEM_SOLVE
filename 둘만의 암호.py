def solution(s, skip, index):
    skip = set(skip)
    answer = ''

    for ch in s:
        i = 1
        next_ch = ''
        cur_index = index
        while i <= cur_index:
            next_ch = chr(((ord(ch) - 97) + i) % 26 + 97)
            i += 1
            if next_ch in skip:
                cur_index += 1
        answer += next_ch

    return answer
