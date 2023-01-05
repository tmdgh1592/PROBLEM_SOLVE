X, K = map(int, input().split())
X *= 1000
a, b, c = 0, 0, 0

# K가 3층의 눈덩이 부피인 경우
if(K*1750 <= X):
    a = K*1750

# K가 2층의 눈덩이 부피인 경우
if(K*3500 <= X):
    b = K*3500

# K가 1층의 눈덩이 부피인 경우
if(K*7000 <= X):
    c = K*7000

print(max(a, b, c))
