def solution(numbers, hand):
    answer = ''
    left_num = 10
    right_num = 11
    num_xy = [(1, 0), (0, 3), (1, 3), (2, 3), (0, 2),  # 0 1 2 3 4
              (1, 2), (2, 2), (0, 1), (1, 1), (2, 1),  # 5 6 7 8 9
              (0, 0), (2, 0)]                            # 10 11

    for num in numbers:

        if num in [1, 4, 7]:
            answer += 'L'
            left_num = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right_num = num
        else:
            press_num = num_xy[num]

            left_dis = (abs(press_num[0] - num_xy[left_num][0]))\
                + abs(press_num[1] - num_xy[left_num][1])

            right_dis = abs((press_num[0] - num_xy[right_num][0]))\
                + abs(press_num[1] - num_xy[right_num][1])

            if left_dis > right_dis or (left_dis == right_dis and hand == 'right'):
                answer += 'R'
                right_num = num
            elif left_dis < right_dis or (left_dis == right_dis and hand == 'left'):
                answer += 'L'
                left_num = num

    return answer
