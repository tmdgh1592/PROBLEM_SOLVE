def solution(babbling):
    answer = 0
    speakable = {"aya", "ye", "woo", "ma"}

    for word in babbling:
        prev = ''
        words = ''
        for ch in word:
            words += ch
            if words in speakable:
                if prev == words: break
                prev = words
                words = ''
        else:
            if words == '': answer += 1

    return answer
