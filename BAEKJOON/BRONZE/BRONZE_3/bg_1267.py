N = int(input())

arr = list(map(int, input().split()))

ys_sum = 0
ms_sum = 0

for x in arr:
    ys_sum += (x // 30) * 10 + 10
    ms_sum += (x // 60) * 15 + 15

if(ys_sum < ms_sum):
    print('Y %d' % ys_sum)
elif(ms_sum < ys_sum):
    print('M %d' % ms_sum)
else:
    print('Y M %d' % ys_sum)
