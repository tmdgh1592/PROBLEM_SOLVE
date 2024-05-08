from collections import defaultdict


def solution(enroll, referral, sellers, amount):
    def f(name, money):
        if money == 0: return
        change = money // 10
        my_money = money - change

        incomes[name] += my_money

        if parent[name] != '-':
            f(parent[name], change)

    parent = dict()
    incomes = defaultdict(int)
    for a, b in zip(enroll, referral):
        parent[a] = b

    amount = map(lambda x: x * 100, amount)

    for seller, money in zip(sellers, amount):
        f(seller, money)

    return [incomes[name] for name in enroll]