
counts = {}
length = 0

with open("input.txt") as f:
	lines = f.readlines()
	length = len(lines)

	for x, line in enumerate(lines):
		current_score = 0

		line = line.strip()

		parts = line.split("|")
		winning = parts[0].split(":")[1].split()
		yours = parts[1].split()

		winning_set = {int(i) for i in winning}


		for num in yours:
			if (int(num) in winning_set):
				current_score += 1

		counts[x] = current_score

ans = {}
total = 0

for at in range(length)[::-1]:
	# print(ans)
	# total += get_score(counts, i)

	to_add = 1
	if (counts[at] > 0):

		for i in range(counts[at]):
			if (at + i + 1 in ans):
				to_add += ans[at+i + 1]

	ans[at] = to_add
	# print("at:", at, counts[at], to_add)
	total += ans[at]

# print(counts)
# print(ans, sum(ans.values()))
print(total)
