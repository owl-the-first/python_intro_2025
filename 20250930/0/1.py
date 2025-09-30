def average(a, *args):
    return sum([a, *args]) / (len(args) + 1)

print(average(1, 3, 5, 7))