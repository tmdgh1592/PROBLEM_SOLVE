def solution(elements):
    n = len(elements)
    answer = set()
    for i in range(n):
        s, e = 0, i
        msum = sum(elements[s:e + 1])
        answer.add(msum)
        while s < n - 1:
            msum -= elements[s]
            s += 1
            e += 1
            msum += elements[e % n]
            answer.add(msum)

    return len(answer)
