def solution(s):
    mdict = {}
    answer = []
    for i, ch in enumerate(s):
        answer.append(-1 if ch not in mdict else i - mdict[ch])
        mdict[ch] = i
    return answer