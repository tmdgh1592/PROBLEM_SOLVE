A, B = map(int, input().split())
# X + Y = A
# X - Y = B

# 합은 항상 차보다 켜야합니다.
# 합과 차의 합은 항상 짝수입니다.
if((A < B or (A+B) % 2 != 0)):
    print(-1)
else:
    X = int((A+B)/2)
    Y = int((A-B)/2)
    print(max(X, Y), min(X, Y))
