# 식을 입력받습니다.
# '-'를 기준으로 분리합니다.
exp_list = input().split('-')

# '-'를 기준으로 나눈 첫번째식은 무조건 양수이므로 초기값으로 설정
result = sum(map(int, exp_list[0].split('+')))

# 1번부터 n번째 묶음식을 빼줍니다.
for i in range(1, len(exp_list)):
    e = map(int, exp_list[i].split('+'))
    result -= sum(e)

print(result)
