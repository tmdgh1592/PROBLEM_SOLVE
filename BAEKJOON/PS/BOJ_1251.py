word = input()
words = []
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        sub1 = word[:i][::-1]
        sub2 = word[i:j][::-1]
        sub3 = word[j:][::-1]
        words.append(sub1+sub2+sub3)

print(sorted(words)[0])
