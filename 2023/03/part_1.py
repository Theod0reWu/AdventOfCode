
symbols = set()
nums = []
width = 0

with open("input.txt") as f:
	lines = f.readlines()
	width = len(lines[0])
	y = 0
	while (y < len(lines)):
		x = 0
		line = lines[y]
		while (x < len(line)):
			# print(line[x])
			if (line[x] == '.'):
				x += 1
			# elif (line[x].isdigit() or (at < width and line[at] == '-' and line[at+1].isdigit())):
			elif (line[x].isdigit()):
				at = x+1
				while (line[at].isdigit()):
					at += 1

				nums.append([int(line[x:at]), (x,y)])

				x = at
			elif (not line[x].isspace()):
				symbols.add((x,y))
				x += 1
			else:
				x += 1
		y+=1

total = 0
for num in nums:
	position = num[1]

	to_check = []

	to_check.append((position[0] - 1, position[1]))
	to_check.append((position[0] + len(str(num[0])), position[1]))

	for i in range(-1,len(str(num[0])) + 1):
		to_check.append((position[0] + i, position[1] - 1))
		to_check.append((position[0] + i, position[1] + 1))

	# print(to_check, num)
	for pos in to_check:
		if (pos in symbols):
			total += num[0]
			# print(num[0])
			break

print(total)

