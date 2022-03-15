from itertools import permutations

op_list = list(permutations(['+', '-', '*'], 2))
num_list = list(permutations(input().split(), 3))

max_result = 0

for op in op_list:
    for num in num_list:
        a, b, c = num[0], num[1], num[2]
        new_result = eval(a + op[0] + b + op[1] + c)
        max_result = max(max_result, new_result)

print(max_result)
