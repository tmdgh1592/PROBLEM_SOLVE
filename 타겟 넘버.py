numbers = []
target = 0


def f(sum, i):
    if i == len(numbers): return 1 if sum == target else 0

    plus_res = f(sum + numbers[i], i + 1)
    sub_res = f(sum - numbers[i], i + 1)
    return plus_res + sub_res


def solution(nums, tar):
    global numbers, target
    numbers = nums
    target = tar

    return f(0, 0)