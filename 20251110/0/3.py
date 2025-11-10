A = type('AA', (), {'__f' : 123})
B = type('BB', (A, ), {'__f' : 456})
print(A.__f)
print(B.__f)

