import sys
from collections import Counter
input = sys.stdin.readline

my_str = str(input().rstrip()).lower() # 문자열을 입력받아 \n 을 제거합니다.
my_counter = Counter(my_str) # Counter 객체 생성

two_most = my_counter.most_common(n=2) # 빈도수 높은 상위 2개의 tuple 리스트를 받아온다.
if(len(two_most) > 1 and two_most[0][1] == two_most[1][1]): # 반환된 리스트의 원소 개수가 2개 이상이고, 빈도가 같다면
    print('?')
else:
    print(str(two_most[0][0]).upper())