n = int(input())
limit_list = sorted(map(int, input().split()), reverse=True)
m = int(input())
boxes = sorted(map(int, input().split()), reverse=True)

time, count = 0, 0

if limit_list[0] < boxes[0]:
    time = -1
else:
    while(count != m):
        # 반복문 하나당 1초 증가
        time += 1

        for limit in limit_list:
            for i in range(len(boxes)):
                if boxes[i] <= limit:
                    count += 1
                    del boxes[i]
                    break

print(time)
