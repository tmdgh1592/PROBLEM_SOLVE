def solution(A):
    start, end = 0, 0
    max_length = 1
    flag = True

    for end in range(len(A)-2):
        if (A[end] >= 0 and A[end+1] <= 0 and A[end+2] >= 0) or\
           (A[end] <= 0 and A[end+1] >= 0 and A[end+2] <= 0):
            flag = True
            continue
        else:
            flag = False

            if start != end:
                max_length = max(max_length, (end+2 - start))
            start = end + 1

    if flag:
        if start != end:
            max_length = max(max_length, (end+2 - start))

    return max_length
