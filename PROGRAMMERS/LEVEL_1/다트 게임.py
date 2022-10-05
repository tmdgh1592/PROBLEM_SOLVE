import re

def solution(dartResult):
    result = []
    bonuses = {'S':1, 'D':2, 'T':3}
    options = {'*':[], '#':[]}
    idx = -1
    nums = re.findall('[\d]+', dartResult)
    opers = re.findall('[A-Z]', dartResult)

    for i in range(len(nums)):
        num = int(nums[i])
        oper = bonuses[opers[i]]
        result.append(pow(num, oper))

    for ch in dartResult:
        if ch.isalpha(): idx += 1
        elif ch == '*' or ch == '#':
            options[ch].append(int(idx))

    for option, idx_list in options.items():
        for idx in idx_list:
            if option == '#': result[idx] *= -1
            else:
                if idx == 0:
                    result[idx] *= 2
                else:
                    result[idx] *= 2
                    result[idx-1] *= 2

    return sum(result)