while True:
    arr = input()
    if(arr == '-1'):
        break

    arr = list(map(int, arr.split()))

    result = 0
    for x in arr:
        if (x * 2) in arr:
            result += 1

    print(result - 1)
