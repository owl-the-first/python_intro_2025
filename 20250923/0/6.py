lst1 = [i*2+1 for i in range(10) if i != 6]
print(lst1)

lst2 = [i*10+j for i in range(5) if i != 2 for j in range(5)]
print(lst2)

a = [[0]*4 for i in range(3)] # правильно делать так список списков
