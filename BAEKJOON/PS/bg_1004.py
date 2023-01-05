T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    count = 0
    n = int(input())

    for _ in range(n):
        x, y, r = map(int, input().split())

        if (x-x1) ** 2 + (y-y1) ** 2 < r ** 2\
                and\
                (x-x2) ** 2 + (y-y2) ** 2 < r ** 2:
            continue

        if (x-x1) ** 2 + (y-y1) ** 2 < r ** 2\
                or\
                (x-x2) ** 2 + (y-y2) ** 2 < r ** 2:
            count += 1

    print(count)
