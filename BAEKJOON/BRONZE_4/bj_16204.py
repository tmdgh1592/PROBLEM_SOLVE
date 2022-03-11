N, M, K = map(int, input().split())

# 양면 모두 O가 적혀 있는 카드 수
sum = K if M > K else M

X1 = N-K  # 앞면에 X가 적혀있는 카드 개수
X2 = N-M  # 뒷면에 X가 적혀있는 카드 개수

# 앞면과 뒷면 모두 X가 적혀있는 카드 수
sum += X1 if X1 < X2 else X2

print(sum)