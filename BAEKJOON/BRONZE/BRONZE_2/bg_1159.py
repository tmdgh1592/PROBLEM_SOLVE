n = int(input())
arr = [input() for _ in range(n)]

result = []

for i in range(97, 123):
    count = 0
    for x in arr:
        if x[0] == chr(i):
            count += 1
        if count == 5:
            result.append(x[0])
            break

if len(result) == 0:
    print('PREDAJA')
else:
    print(''.join(result))
