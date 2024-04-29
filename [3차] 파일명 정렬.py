from functools import cmp_to_key


def compare(item1, item2):
    s = -1
    head1, number1 = '', ''
    for i, ch in enumerate(item1):
        if ch.isdigit() and s == -1:
            head1 = item1[:i]
            s = i
        if not ch.isdigit() and s != -1:
            number1 = item1[s:i]
            break
    if number1 == '':
        number1 = item1[s:]
    head1 = head1.upper()
    number1 = int(number1)

    s = -1
    head2, number2 = '', ''
    for i, ch in enumerate(item2):
        if ch.isdigit() and s == -1:
            head2 = item2[:i]
            s = i
        if not ch.isdigit() and s != -1:
            number2 = item2[s:i]
            break
    if number2 == '':
        number2 = item2[s:]
    head2 = head2.upper()
    number2 = int(number2)

    if head1 == head2:
        if number1 == number2:
            return 0
        if number1 > number2:
            return 1
        if number1 < number2:
            return -1
    elif head1 > head2:
        return 1
    else:
        return -1


def solution(files):
    return sorted(files, key=cmp_to_key(compare))