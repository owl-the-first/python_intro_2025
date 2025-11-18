with open('o', 'w+') as fl:
    print('Hello, world!\nIm a student\n', file = fl)

# with open('o', 'rb') as file:
#     file.readlines()

with open('o', 'r+') as fl:
    print(*sorted(fl.readlines()), file = fl)
