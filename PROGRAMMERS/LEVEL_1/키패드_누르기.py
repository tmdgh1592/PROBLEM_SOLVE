def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    distance = {
        '*' : [4, 3, 2, 1],
        '#' : [4, 3, 2, 1],
        0 : [3, 2, 1, 0],
        1 : [1, 2, 3, 4],
        2 : [0, 1, 2, 3],
        3 : [1, 2, 3, 4],
        4 : [2, 1, 2, 3],
        5 : [1, 0, 1, 2],
        6 : [2, 1, 2, 3],
        7 : [3, 2, 1, 2],
        8 : [2, 1, 0 ,1],
        9 : [3, 2, 1, 2]
    }
    converter = {2 : 0, 5 : 1, 8 : 2, 0 : 3}

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right = number
        else:        
            left_dist = distance[left][converter[number]]
            right_dist = distance[right][converter[number]]
            
            if left_dist < right_dist:
                answer += 'L'
                left = number
            elif left_dist > right_dist:
                answer += 'R'
                right = number
            else:
                if hand == 'right':
                    answer += 'R'
                    right = number
                else:
                    answer += 'L'
                    left = number

    return answer