# 12 red cubes, 13 green cubes, and 14 blue cubes

with open("input.txt") as f:
	lines = f.readlines()

	total = 0
	for line in lines:
		game_id = line.split(":")

		game = game_id[1].split(";")
		game_id = int(game_id[0][5:])

		min_cubes = [-1,-1,-1]

		for turn in game:
			x = turn.split(",")

			for c in x:
				t = c.split()
				num = int(t[0])

				if (t[1] == "red" and (num > min_cubes[0] or min_cubes[0] == -1)):
					min_cubes[0] = num
				if (t[1] == "green" and (num > min_cubes[1] or min_cubes[1] == -1)):
					min_cubes[1] = num
				if (t[1] == "blue" and (num > min_cubes[2] or min_cubes[2] == -1)):
					min_cubes[2] = num

		total += min_cubes[0] * min_cubes[1] * min_cubes[2]
		# print(min_cubes)
		# print(total)
	print(total)