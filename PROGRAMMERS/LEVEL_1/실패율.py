from bisect import bisect_left, bisect_right 

def count_by_range(arr, left, right):
    return bisect_right(arr, right) - bisect_left(arr, left)

def solution(n, stages):
    answer = []
    stages.sort()
    top_stage = max(stages)
    
    # i 개수 / i보다 크거나 같은 수
    for stage in range(1, n+1):
        child = count_by_range(stages, stage, stage)
        parent = count_by_range(stages, stage, top_stage)
        count = child / parent if parent else 0
        
        answer.append((count, stage))
        
    answer.sort(key = lambda x:(-x[0], x[1]))
    answer = [i for _, i in answer]
    
    return answer

print(solution(5, [1,1,1,3,4]))
