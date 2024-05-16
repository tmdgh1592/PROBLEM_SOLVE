import sys

sys.setrecursionlimit(int(1e6))


#  전위 순회 : Root - Left - Right
#  후위 순회 : Left - Right - Root
def solution(nodeinfo):
    answer = [[], []]
    nodeinfo = sorted([(num + 1, x, y) for num, (x, y) in enumerate(nodeinfo)], key=lambda x: x[1])

    def f(arr):
        if not arr: return

        root = (0, -1, 0)  # idx, y, num
        for i, (num, x, y) in enumerate(arr):
            if root[1] < y: root = (i, y, num)

        answer[0].append(root[2])
        f(arr[:root[0]])
        f(arr[root[0] + 1:])
        answer[1].append(root[2])

    f(nodeinfo)
    return answer
