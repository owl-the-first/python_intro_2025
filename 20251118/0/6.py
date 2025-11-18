import pickle
import sys

class SerCls:
    lst = [1, 2, 3]
    dct = {i: 2*i + 1 for i in range(5)}
    num = 100500
    st = 'Привет'

sc = SerCls()

sc.lst.append(4)
sc.dct['QQ'] = 'QKRQ'
sc.num = 42
sc.st = 'HEHE'

with open(sys.argv[1], 'bw+') as fout:
    pickle.dump(sc, fout, protocol=0)

del sc

with open(sys.argv[1], 'rb') as fin:
    sc1 = pickle.load(fin)

print(sc1.lst, sc1.dct, sc1.num, sc1.st)
