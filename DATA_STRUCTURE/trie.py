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
        if '*' not in cur:
            return False
        return True


trie = Trie()

trie.add('Hello')
trie.add('Hel')

print(trie.search('H'))
print(trie.search('He'))
print(trie.search('Hel'))
print(trie.search('Helo'))
print(trie.search('Hello'))