from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for str in strs:
            words[''.join(sorted(str))].append(str)

        return list(words.values())