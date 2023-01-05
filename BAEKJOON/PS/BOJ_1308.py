import datetime


y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
d_day = int(str(datetime.date(y2, m2, d2) -
            datetime.date(y1, m1, d1)).split()[0])

over = 0
for y in range(1000):
    if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
        over += 366
    else:
        over += 365

if d_day >= over:
    print('gg')
else:
    print(f'D-{d_day}')