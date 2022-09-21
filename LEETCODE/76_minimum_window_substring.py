from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, ch in enumerate(s, 1):
            missing -= need[ch] > 0
            need[ch] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                if not end or right - left < end - start:
                    start, end = left, right
                
                need[s[left]] += 1
                left += 1
                missing += 1
        
        return s[start:end]