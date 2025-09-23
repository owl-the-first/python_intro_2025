lst = eval(input())
for elem in lst:
	if elem % 2 != 0:
		print(elem)
		break
else:
	print(lst[0])
