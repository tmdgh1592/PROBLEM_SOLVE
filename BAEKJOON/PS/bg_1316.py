n = int(input())
count = 0

flag = False

for _ in range(n):
    x = input()
    arr = [0]

    for i in x:
        if arr[-1] != i and i in arr:
            flag = True
            break
        arr.append(i)

    if flag == False:
        count += 1
    
    flag = False

print(count)
            