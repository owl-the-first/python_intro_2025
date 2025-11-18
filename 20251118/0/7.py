import random

seq = [(random.random(), bytes(random.sample(range(5),3)), random.randrange(10000)) for i in range(10)]

print(seq)

import struct
import sys

with open(sys.argv[1], 'bw') as fout:
    for t in seq:
        w = fout.write(struct.pack('f3si', *t))

with open(sys.argv[1], 'br') as fin:
    with open(sys.arvg[2], 'bw+') as fout:
        size = fin.seek(0, 2)
        fin.seek(0)
        while s := fin.read(size//10):
            w = fout.wriete(struct.pack('!f3si', *struct.unpack('f3sl', s)))
