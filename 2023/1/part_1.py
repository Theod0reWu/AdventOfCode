
total = 0
with open ("input.txt") as f:
	x = f.read().split()
	for line in x:
		# print(line, line[0], line[-1])
		num = ""
		for c in line:
			if (c.isdigit()):
				num += c
				break
		for c in range(0,len(line))[::-1]:
			# print(c)
			if (line[c].isdigit()):
				num += line[c]
				break
		num = int(num)
		total += num

print(total)