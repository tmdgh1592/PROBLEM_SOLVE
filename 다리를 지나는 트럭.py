from collections import deque


def solution(max_size, max_weight, truck_weights):
    truck_weights = deque([(weight, 0) for weight in truck_weights])
    cur_weight = 0
    time = 0
    running = deque([])

    while truck_weights:
        time += 1
        weight, pos = truck_weights[0]

        # 건너고 있는 트럭 위치 1씩 update
        for i in range(len(running)):
            r_weight, r_pos = running.popleft()
            if r_pos + 1 > max_size:
                cur_weight -= r_weight
            else:
                running.append((r_weight, r_pos + 1))

        # 트럭이 더 지날 수 있는 경우
        if cur_weight + weight <= max_weight and len(running) < max_size:
            running.append((weight, 1))
            cur_weight += weight
            truck_weights.popleft()

    while running:
        time += 1
        # 건너고 있는 트럭 위치 1씩 update
        for i in range(len(running)):
            weight, pos = running.popleft()
            if pos + 1 <= max_size:
                running.append((weight, pos + 1))

    return time
