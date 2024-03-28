def solution(numbers):
    if not sum(numbers): return '0'
    numbers = sorted(map(str, numbers), key=lambda x:x*3, reverse=True)
    return ''.join(numbers)