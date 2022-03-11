H, M, S = map(int, input().split())
cook_time = int(input())

total_time = \
    H * 60 * 60 + \
    M * 60 + \
    S + \
    cook_time

end_h = (total_time // (60 * 60)) % 24
total_time %= (60 * 60)

end_m = total_time // (60)
total_time %= (60)

end_s = total_time

print(end_h, end_m, end_s)
