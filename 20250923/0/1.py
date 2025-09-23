a = list(range(5, 16))
b = [chr(c) for c in range(ord('a'), ord('k'))]
a[4:7+1] = b[-5:]
print(a, b)
