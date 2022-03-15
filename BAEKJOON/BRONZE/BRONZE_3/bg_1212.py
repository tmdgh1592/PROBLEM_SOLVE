oct_n = input()  # 8진수를 입력받습니다.

ans = bin(int(oct_n, 8))  # 8진수 str을 10진수로 변환 후, 다시 2진수로 변환

print(str(ans).removeprefix('0b'))