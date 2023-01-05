import math
A, B, C = map(int, input().split())

if(B >= C):
    print(-1)
else:
    # 손익 분기점 식
    X = math.floor(A / (C-B)) + 1

    if(X < 0):
        print(-1)
    else:
        print(X)
