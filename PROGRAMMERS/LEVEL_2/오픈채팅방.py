def solution(record):
    answer = []
    user_dict = dict()  # {uid : name}

    for log in record:
        text = log.split()
        if len(text) > 2:
            user_dict[text[1]] = text[2]

    for log in record:
        text = log.split()
        if text[0] == "Enter":
            answer.append(f'{user_dict[text[1]]}님이 들어왔습니다.')
        elif text[0] == "Leave":
            answer.append(f'{user_dict[text[1]]}님이 나갔습니다.')

    return answer
