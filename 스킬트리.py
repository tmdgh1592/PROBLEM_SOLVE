import heapq


def solution(operations):
    max_q, min_q = [], []
    remain = 0

    for data in operations:
        op, num = data.split()
        num = int(num)

        if op == 'I':
            heapq.heappush(max_q, -num)
            heapq.heappush(min_q, num)
            remain += 1
        elif op == 'D':
            if remain == 0: continue
            if num == -1:
                heapq.heappop(min_q)
            else:
                heapq.heappop(max_q)
            remain -= 1
        if remain == 0:
            min_q.clear()
            max_q.clear()

    if remain == 0:
        return [0, 0]
    else:
        return [-heapq.heappop(max_q), heapq.heappop(min_q)]