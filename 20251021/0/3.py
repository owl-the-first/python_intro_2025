def pri(seq):
    print(*seq)

pri(i*2+1 for i in range(10) if i%3)
