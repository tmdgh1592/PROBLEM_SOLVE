from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = set()
    s = []

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            s.append(s.pop(s.index(city)))
        else:
            answer += 5
            cache.add(city)
            s.append(city)
            if len(cache) > cacheSize:
                cache.discard(s.pop(0))

    return answer