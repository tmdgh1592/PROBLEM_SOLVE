a, b = map(int, input().split())
a, b = a-1, b-1

dis_w = abs(b//4 - a//4)
dis_h = abs(b % 4 - a % 4)

print(dis_w + dis_h)
