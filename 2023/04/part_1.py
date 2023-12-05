
with open("input.txt") as f:
	lines = f.readlines()

	total = 0
	for line in lines:
		current_score = 0

		line = line.strip()

		parts = line.split("|")
		winning = parts[0].split(":")[1].split()
		yours = parts[1].split()

		winning_set = {int(i) for i in winning}


		for num in yours:
			if (int(num) in winning_set):
				current_score += 1

		if (current_score > 0):
			total += 2 ** (current_score -1)

	print(total)
