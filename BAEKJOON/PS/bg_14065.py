X = float(input())

gallen_per_mile = (1.609344 / 3.785411784)
ans = (100.0 / (gallen_per_mile * X))

print('%.6f' % ans)
