from itertools import permutations
import re

priority = list(permutations(['+', '-', '*']))


def solution(expression):
    answer = 0
    org_nums = re.split(r'\D', expression)
    org_ops = re.split(r'\d+', expression)[1:-1]

    for pri in priority:
        nums = org_nums.copy()
        ops = org_ops.copy()

        for p in pri:  # pri = (+, -, *)
            i = 0
            while i < (len(ops)):
                if p == ops[i]:
                    nums[i] = str(eval(nums[i] + p + nums[i+1]))
                    del nums[i+1]
                    del ops[i]
                    continue
                i += 1

        answer = max(answer, abs(int(nums[0])))
    return answer
