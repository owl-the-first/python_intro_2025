for i in range(12, 23):
    print(f"{bin(i)} = {hex(i)}")
print()

def bih(a, b):
    bw, hw = len(bin(b)), len(hex(b))
    for j in range(a, b + 1):
        print(f"{j:>#{bw}b} = {j:#{hw}x}")

bih(12, 86)
