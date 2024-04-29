def valid(mstr):
    s = []

    for x in mstr:
        if x == '(':
            s.append(x)
        elif x == ')' and s and s[-1] == '(':
            s.pop()
        else:
            return False
    return not s


def solution(p):
    if p == '': return p
    left, right = 0, 0

    for x in p:
        if x == '(': left += 1
        if x == ')': right += 1
        if left == right: break
    next = left + right
    u = p[:next]
    v = p[next:]

    if valid(u):
        return u + solution(v)
    else:
        tmp = '(' + solution(v) + ')'
        u = u[1:len(u) - 1]

        for x in u:
            if x == '(': tmp += ')'
            if x == ')': tmp += '('
        return tmp
