from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, nowTemp in enumerate(temperatures):
            while stack and nowTemp > temperatures[stack[-1]]:
                prevIdx = stack.pop()
                answer[prevIdx] = i - prevIdx

            stack.append(i)
        
        return answer