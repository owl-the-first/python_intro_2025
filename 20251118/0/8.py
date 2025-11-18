import sys, binascii, pathlib

file = pathlib.Path(sys.argv[1])
i = 0
while i < len(file.read_bytes()):
    print(binascii.hexlify(file.read_bytes()[i: i + 16, 'b']))
    i += 16
