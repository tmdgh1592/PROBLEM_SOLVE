n, f = [int(input()) for _ in range(2)]


def getTwoNum(n, f):
    a = n - (n % 100)
    while a % f != 0:
        a += 1
    return str(a)[-2:]


print(getTwoNum(n, f))
