# with open('file1', 'br') as fl:
#     fl.seek(10)
#     for i in range(40):
#         print(fl.read(1))

# print('-----------------------------')

# with open('file2', 'br') as fl:
#     fl.seek(1)
#     for i in range(40):
#         print(fl.read(1))

# print('-----------------------------')

import sys

with open(sys.argv[1], 'br') as fin:
    bins = fin.read()
    with open(sys.argv[1], 'wb') as fout:
        print(bins)
        fout.write(bins[len(bins)//2:] + bins[:len(bins)//2])
