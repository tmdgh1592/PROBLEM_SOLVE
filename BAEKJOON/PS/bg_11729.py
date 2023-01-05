n = int(input())
count = 0

# 한개 움직이는 것을 프린트
move = []

def hanoi(n, start, mid, end):
    global count

    if n == 1:
        move.append((start, end))
        count += 1
        return
    hanoi(n-1, start, end, mid)
    move.append((start, end))
    count += 1
    hanoi(n-1, mid, start, end)


hanoi(n, 1, 2, 3)
print(count)
for (n, m) in move:
    print(f'{n} {m}')
