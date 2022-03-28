import sys
input = sys.stdin.readline


class Trie:

    head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            return True
        else:
            return False


count = 0
n, m = map(int, input().split())
dictionary = Trie()
for _ in range(n):
    dictionary.add(input())
for _ in range(m):
    count += 1 if dictionary.search(input()) else 0

print(count)
