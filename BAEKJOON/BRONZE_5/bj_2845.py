import sys
input = sys.stdin.readline

# L : 1m2당 사람의 수
# P : 파티장 면적
L, P = map(int, input().split())
people_list = list(map(int, input().split()))

LP = L * P

for people_count in people_list:
    print(people_count - LP, end=' ')