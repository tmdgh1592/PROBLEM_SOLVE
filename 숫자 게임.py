import heapq


def solution(A, B):
    a = [-x for x in A]
    b = [-x for x in B]
    heapq.heapify(a)
    heapq.heapify(b)

    answer = 0

    while a and b:
        aa = -heapq.heappop(a)
        bb = -heapq.heappop(b)

        if aa < bb:
            answer += 1
        else:
            heapq.heappush(b, -bb)

    return answer
