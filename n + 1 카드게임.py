from collections import deque

target = 0


def check(a, b):
    for c in a:
        if target - c in b:
            a.remove(c)
            b.remove(target - c)
            return True
    return False


def solution(coin, cards):
    global target

    answer, cur = 1, 0
    n = len(cards)
    target = n + 1
    hands = deque(cards[:n // 3])
    cards = deque(cards[n // 3:])
    deck = []

    while cards:
        deck.append(cards.popleft())
        deck.append(cards.popleft())

        if check(hands, hands):
            pass
        elif coin >= 1 and check(hands, deck):
            coin -= 1
        elif coin >= 2 and check(deck, deck):
            coin -= 2
        else:
            break

        answer += 1

    return answer
