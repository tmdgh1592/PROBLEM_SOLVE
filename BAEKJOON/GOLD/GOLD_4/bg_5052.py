import sys
input = sys.stdin.readline


class Trie:
    head = {}
    arr = []

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True
        self.arr.append(word)

    def is_consistent(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if cur['*'] and len(cur) == 1:
            return True
        else:
            return False

    def init(self):
        self.head = {}
        self.arr = []


for _ in range(int(input())):
    n = int(input().rstrip())
    trie = Trie()
    trie.init()
    is_cons = True

    for _ in range(n):
        trie.add(input().rstrip())
    for word in trie.arr:
        if not trie.is_consistent(word):
            is_cons = False
            break

    print('YES') if is_cons else print('NO')
