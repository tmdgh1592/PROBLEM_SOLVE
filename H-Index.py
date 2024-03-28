def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i in range(len(citations)):
        left=citations[i]
        if i == len(citations)-1:
            right = 0
        else:
            right = citations[i+1]

        if left >= i+1 and right <= i+1:
            answer = i+1

    return answer