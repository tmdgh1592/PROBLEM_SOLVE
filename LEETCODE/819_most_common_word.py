from collections import defaultdict
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(
            r'\W', ' ', paragraph).lower().split() if word not in banned]
        word_dict = defaultdict(int)
        for word in words:
            word_dict[word] += 1

        return max(word_dict, key=word_dict.get)
