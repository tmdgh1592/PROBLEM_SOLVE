#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

for _ in range(int(input())):
    n, m = MIS()
    arr = list(MIS())
    index_list = [i for i in range(n)]
    q = deque(zip(index_list, arr))
    seq = 0


    def find_bigger(q, value):
        # 코드 라인은 줄일 수 있지만, 전체 큐 전체를 확인해야 해서 시간이 더 많이 소모 됨.
        # return True if max(q, key=lambda x:x[1])[1] > value else False

        for i in range(1, len(q)):
            if q[i][1] > value:
                return True
        
        return False


    while True:
        idx, value = q[0]

        if find_bigger(q, value):
            q.append(q.popleft())
        else:
            q.popleft()
            seq += 1
            if idx == m:
                print(seq)
                break