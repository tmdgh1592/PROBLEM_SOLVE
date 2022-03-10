import sys
input = sys.stdin.readline

M = str(input()) # 최대 길이 6글자인 16진수를 입력받는다.
print(int(M, 16)) # 16진수 -> 10진수 변환