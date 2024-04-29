import sys
sys.setrecursionlimit(int(1e6))

INF = int(1e9)
dp = {}


def solution(target):
    def f(value):
        if value == 0:
            return [0, 0]
        if value in dp:
            return dp[value]

        data, msinbol = INF, -INF
        if value - 50 >= 0:
            a, b = f(value - 50)
            a += 1
            b += 1
            if a < data:
                data = a
                msinbol = b
            elif a == data and b > msinbol:
                msinbol = b

        for i in range(1, 21):
            if value - i * 3 >= 0:
                a, b = f(value - i * 3)
                a += 1
                if a < data:
                    data = a
                    msinbol = b
                elif a == data and b > msinbol:
                    msinbol = b
            if value - i * 2 >= 0:
                a, b = f(value - i * 2)
                a += 1
                if a < data:
                    data = a
                    msinbol = b
                elif a == data and b > msinbol:
                    msinbol = b
            if value - i >= 0:
                a, b = f(value - i)
                a += 1
                b += 1
                if a < data:
                    data = a
                    msinbol = b
                elif a == data and b > msinbol:
                    msinbol = b

        dp[value] = [data, msinbol]
        return dp[value]

    return f(target)