from itertools import permutations


def solution(n, weak, dist):
    dist.sort(reverse=True)
    wk = len(weak)
    weak += [i + n for i in weak]

    for i in range(1, len(dist) + 1):
        for friend in permutations(dist[:i]):
            for sp in range(wk):
                weaks = weak[sp: sp + wk]
                friends = list(friend[:])

                while friends and weaks:
                    friend_dist = friends.pop(0)
                    sp = weaks.pop(0)
                    dst = sp + friend_dist

                    while weaks and weaks[0] <= dst:
                        weaks.pop(0)

                if len(weaks) == 0:
                    return i
    return -1
