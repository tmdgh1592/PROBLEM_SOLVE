def f(x):
    if x == '1': return [0, 0]

    n = len(x)
    x = x.replace('0', '')
    zero_cnt = n - len(x)
    a, b = f(bin(len(x))[2:])
    return [a + 1, zero_cnt + b]


def solution(s):
    return f(s)