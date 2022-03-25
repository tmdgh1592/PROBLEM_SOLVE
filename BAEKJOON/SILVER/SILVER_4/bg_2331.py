A, P = input().split()
arr = [A]
P = int(P)

prev = A
while arr.count(prev) < 2:
    prev = str(sum([int(i) ** P for i in prev]))
    arr.append(prev)

i = arr.index(prev)

print(len(arr[:i]))
