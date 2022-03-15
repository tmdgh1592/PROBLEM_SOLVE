while True:
    num = input()

    if(num == '0'):
        break

    total_len = 2 + (len(num)-1)

    for e in num:
        if(e == '0'):
            total_len += 4
        elif(e == '1'):
            total_len += 2
        else:
            total_len += 3

    print(total_len)
