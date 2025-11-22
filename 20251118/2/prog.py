import sys


for i in sys.stdin:
    sys.stdout.write(i.encode('latin1', errors='replace').decode('cp1251', errors='replace'))
