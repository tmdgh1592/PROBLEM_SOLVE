from itertools import product
from bisect import bisect_right


def solution(word):
    dictionary = ['A', 'E', 'I', 'O', 'U']

    for i in range(2, 6):
        for w in product('AEIOU', repeat=i):
            dictionary.append(''.join(w))
    return bisect_right(sorted(dictionary), word)