def jinsoo(n, k):
    a, b = divmod(n, k)
    if a == 0: return str(b)
    return jinsoo(a, k) + str(b)


def soojin(val, k):
    res = 0
    val = val[::-1]
    for i, x in enumerate(val):
        res += int(x) * (k ** i)
    return res


def is_prime(num):
    if num == 0 or num == 1: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True


def solution(n, k):
    transed = jinsoo(n, k)
    data = ''
    answer = 0
    for x in transed:
        if x == '0':
            if data:
                val = soojin(data, 10)
                answer += is_prime(val)
            data = ''
        else:
            data += x
    if data:
        val = soojin(data, 10)
        answer += is_prime(val)

    return answer
