from collections import defaultdict

answer = int(1e9)


def solution(begin, target, words):
    used = defaultdict(bool)

    def f(word, cnt):
        if word == target:
            global answer
            answer = min(answer, cnt)
            return

        for w in words:
            if used[w]: continue
            diff_cnt = 0

            for i in range(len(w)):
                if w[i] != word[i]:
                    diff_cnt += 1

            if diff_cnt == 1:
                used[w] = True
                f(w, cnt + 1)
                used[w] = False

    f(begin, 0)
    return 0 if answer == int(1e9) else answer
