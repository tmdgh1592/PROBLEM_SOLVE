def solution(n, tops):
    left, right = [0] * n, [0] * n
    left[0], right[0] = 2 + tops[0], 1

    for i in range(1, n):
        right[i] = (left[i - 1] + right[i - 1]) % 10007
        left[i] = (right[i - 1] * (1 + tops[i])) % 10007 + (left[i - 1] * (2 + tops[i])) % 10007
    return (left[n - 1] + right[n - 1]) % 10007