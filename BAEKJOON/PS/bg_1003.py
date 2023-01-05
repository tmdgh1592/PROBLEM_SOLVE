
# n의 0과 1 호출 횟수는
# n-1과 n-2에서의 호출 횟수의 합과 같다.
# 점화식 f(n) = f(n-1) + f(n-2)

def fibo(n):
    # DP 테이블
    zero = [1, 0]
    one = [0, 1]

    if n >= 2:
        for i in range(2, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])

    print(zero[n], one[n])


T = int(input())
for _ in range(T):
    fibo(int(input()))
