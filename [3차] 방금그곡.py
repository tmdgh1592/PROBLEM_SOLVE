def parse(time):
    hh, mm = time.split(':')
    return int(hh) * 60 + int(mm)


def trans(song):
    return song.replace('C#', 'H').replace('D#', 'I').replace('F#', 'K').replace('G#', 'L').replace('A#', 'M').replace(
        'B#', 'O')


def solution(m, musicinfos):
    answer = '(None)'
    time = 0
    m = trans(m)

    for infos in musicinfos:
        a, b, title, melody = infos.split(',')
        a, b = parse(a), parse(b)
        melody = trans(melody)

        n = b - a
        song = ''
        for i in range(n):
            song += melody[i % len(melody)]

        if m in song:
            if answer == '(None)':
                answer = title
                time = n
            else:
                if time < n:
                    answer = title
                    time = n

    return answer