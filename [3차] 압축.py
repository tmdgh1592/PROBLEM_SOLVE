mdict = {chr(65+i):i+1 for i in range(26)}

def solution(msg):
    i = 0
    last = 27
    answer = []

    while i < len(msg):
        now = msg[i]
        if i + 1 == len(msg):
            answer.append(mdict[now])
            break

        next = msg[i+1]
        if not mdict.get(now + next):
            mdict[now + next] = last
            last += 1
            answer.append(mdict[now])
            i += 1
        else:
            i += 1
            while mdict.get(now + next) and i < len(msg):
                now += next
                i += 1
                if i == len(msg): break
                next = msg[i]
            answer.append(mdict[now])
            mdict[now + next] = last
            last += 1
        print(list(mdict.items())[26:40])

    return answer