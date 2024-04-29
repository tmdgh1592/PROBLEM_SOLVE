my_dict = {}

def solution(keymap, targets):
    answer = []

    for key in keymap:
        for i, ch in enumerate(key):
            if ch in my_dict:
                my_dict[ch] = min(my_dict[ch], i + 1)
            else:
                my_dict[ch] = i + 1

    for target in targets:
        count = 0
        flag = False
        for ch in target:
            if ch in my_dict:
                count += my_dict[ch]
            else:
                flag = True
        answer.append(-1 if flag else count)

    return answer