from collections import Counter


a = Counter(input().split())
b = Counter(input().split())
if b - a:
    print("No")
else:
    print("True")
