c = int(input())

for _ in range(c):
    n, *arr = map(int, input().split())
    avg = sum(arr)/n
    per = round((len([x for x in arr if x > avg]) / n) * 100, 3)

    print(str(format(per, '.3f')) + '%')
