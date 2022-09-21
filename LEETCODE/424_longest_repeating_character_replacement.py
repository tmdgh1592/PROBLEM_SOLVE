from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counter = Counter()

        for right, ch in enumerate(s, 1):
            counter[ch] += 1
            most_ch_n = counter.most_common(1)[0][1]

            if right - left - most_ch_n > k:
                counter[s[left]] -= 1
                left += 1

        return right - left