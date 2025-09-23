arr = []
while s := input():
	arr.append(list(eval(s)))
for y in range(len(arr)):
	for x in range(y+1, len(arr)):
		arr[y][x], arr[x][y] = arr[x][y], arr[y][x]
for line in arr:
	print(*line)
