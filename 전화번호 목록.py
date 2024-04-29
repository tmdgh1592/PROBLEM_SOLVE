def solution(phone_book):
    phone_book.sort()
    numbers = set()
    for number in phone_book:
        num = ''
        for x in number:
            num += x
            if num in numbers: return False
        numbers.add(number)

    return True