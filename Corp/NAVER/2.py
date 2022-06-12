def solution(S, C):
    count = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            count += min(C[i], C[i+1])

    return count
