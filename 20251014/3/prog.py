import re
from collections import Counter

W = int(input().strip())
lines = []
while True:
    try:
        line = input()
        if line == '':
            break
        lines.append(line)
    except EOFError:
        break
words = re.findall(r'\b[a-zA-Z]{%d}\b' % W, ' '.join(lines).lower())
if words:
    counter = Counter(words)
    popular = sorted([word for word, count in counter.items() if count == max(counter.values())])
    print(' '.join(popular))
