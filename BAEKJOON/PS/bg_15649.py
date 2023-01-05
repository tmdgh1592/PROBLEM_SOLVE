# nPr
n, r = map(int, input().split())
result = []


def permutation(n, r):
    # 종료조건 : 배열에 2개가 들어갔을 때
    if len(result) == r:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n+1):
        if i not in result:  # 중복 허용 안함
            result.append(i)
            permutation(n, r)
            result.pop()


permutation(n, r)
