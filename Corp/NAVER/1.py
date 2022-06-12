def solution(arr):
    on_off_dict = dict()
    count = 0

    for i in range(len(arr)):
        on_off_dict[i] = False

    for num in arr:
        on_off_dict[num-1] = True
        flag = True

        for i in range(num-1):
            if on_off_dict[i] == False:
                flag = False
                break

        if flag:
            count += 1

    return count
