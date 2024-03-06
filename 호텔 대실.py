def parse(time):
    hh, mm = map(int, time.split(':'))
    return hh * 60 + mm


def solution(book_times):
    book_times = sorted([(parse(s), parse(e)) for s, e in book_times])
    answer = 0
    rooms = []

    for i in range(len(book_times)):
        s, e = book_times[i]

        for room in rooms:
            ss, ee = room
            if s >= ee:
                rooms.remove(room)

        if len(rooms) == answer:
            answer += 1

        rooms.append((s, e + 10))

    return answer
