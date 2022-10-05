def convert_10_3(num):
    q, r = divmod(num, 3)
    if q > 0:
        return str(r) + convert_10_3(q)
    return str(r)

def solution(n):
    reversed_n_10_3 = convert_10_3(n)
    print(reversed_n_10_3)
    return int(reversed_n_10_3, 3)