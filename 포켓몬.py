def solution(nums):
    a = len(set(nums))
    b = len(nums) // 2
    return min(a, b)