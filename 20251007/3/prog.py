a = []
while True:
    try:
        s = input()
        if not s:
            break
        a.append(list(s))
    except EOFError:
        break
h, w = len(a), len(a[0])
o = [row[1:-1] for row in a[1:-1]]
o_h = len(o)
o_w = len(o[0])
water = sum(i.count('~') for i in o)
gas = sum(i.count('.') for i in o)
o_v = o_h * o_w
o_new = [['.'] * o_h for i in range(o_w)]
k = 0
for i in range(o_w - 1, -1, -1):
    for j in range(o_h - 1, -1, -1):
        if k < water:
            o_new[i][j] = '~'
            k += 1
rotated = [['#'] * (o_h + 2)]
for i in o_new:
    rotated.append(['#'] + i + ['#'])
rotated.append(['#'] * (o_h + 2))
for i in rotated:
    print(''.join(i))
max_count = max(gas, water)
gas_bar = '.' * round(20 * gas / max_count) if max_count > 0 else 0
water_bar = '~' * round(20 * water / max_count) if max_count > 0 else 0
frac_gas = f"{gas}/{gas + water}"
frac_water = f"{water}/{gas + water}"
max_frac_len = max(len(frac_gas), len(frac_water))
print(f"{gas_bar.ljust(20)} {frac_gas.rjust(max_frac_len)}")
print(f"{water_bar.ljust(20)} {frac_water.rjust(max_frac_len)}")
