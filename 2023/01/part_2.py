
digits = {"one" : "1", "two": "2", "three": "3", "four" : "4", "five" : "5", "six" : "6" , "seven": "7", "eight": "8", "nine": "9"}

total = 0
with open ("input.txt") as f:
	x = f.read().split()
	for line in x:
		num = ""
		for c in range(len(line)):
			if (line[c].isdigit()):
				num += line[c]
				break
			done = False
			for d in digits:
				if (d == line[c:c + len(d)]):
					num += digits[d]
					done = True
					break
			if (done):
				break
		for c in range(0,len(line))[::-1]:
			# print(c)
			if (line[c].isdigit()):
				num += line[c]
				break
			done = False
			for d in digits:
				# print(d, c - len(d) + 1, c + 1)
				if (d == line[c - len(d) + 1: c + 1]):
					num += digits[d]
					done = True
					break
			if (done):
				break
		num = int(num)
		# print(num)
		total += num

print(total)