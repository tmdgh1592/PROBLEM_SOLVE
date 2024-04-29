def solution(data):
    s = []

    for x in data:
        if x == '(': s.append(x)
        if x == ')':
            if not s: return False
            if s[-1] == '(': s.pop()

    return not s