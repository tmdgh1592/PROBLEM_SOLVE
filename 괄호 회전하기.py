from collections import deque


def rotate(q):
    q.append(q.popleft())


def check(q):
    s = []
    while q:
        val = q.popleft()
        if val == '[' or val == '(' or val == '{':
            s.append(val)
        else:
            if not s: return False
            if val == ']' and s.pop() != '[': return False
            if val == ')' and s.pop() != '(': return False
            if val == '}' and s.pop() != '{': return False
    return not s


def solution(s):
    answer = 0
    n = len(s)
    q = deque(list(s))

    for i in range(n):
        answer += check(q.copy())
        rotate(q)
    return answer
