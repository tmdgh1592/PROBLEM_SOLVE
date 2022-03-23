from collections import Counter
import sys
input = sys.stdin.read

sen = input().replace(' ', '').replace('\n', '')
counter = Counter(sen).most_common()
result, most_count = counter[0]

for i in range(1, len(counter)):
    if most_count != counter[i][1]:
        break
    result += counter[i][0]

print(''.join(sorted(result)))
