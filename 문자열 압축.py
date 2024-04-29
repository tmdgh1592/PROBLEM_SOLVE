def solution(s):
    n = len(s)
    answer = n

    for size in range(1, n // 2 + 1):
        compressed = ''
        prev = s[:size]
        cnt = 1
        sen = s[size:]
        while len(sen) >= size:
            now = sen[:size]
            if now == prev:
                cnt += 1
            else:
                if cnt == 1:
                    compressed += prev
                else:
                    compressed += f'{cnt}{prev}'
                cnt = 1
                prev = now
            sen = sen[size:]
        if cnt == 1:
            compressed += prev
        else:
            compressed += f'{cnt}{prev}'
        compressed += sen
        answer = min(answer, len(compressed))
    return answer
