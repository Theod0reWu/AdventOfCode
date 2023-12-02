
# 12 red cubes, 13 green cubes, and 14 blue cubes

with open("input.txt") as f:
	lines = f.readlines()

	total = 0
	for line in lines:
		game_id = line.split(":")

		game = game_id[1].split(";")
		game_id = int(game_id[0][5:])

		add = True

		for turn in game:
			x = turn.split(",")

			for c in x:
				t = c.split()
				num = int(t[0])

				if ((t[1] == "red" and num > 12) or (t[1] == "blue" and num > 14) or (t[1] == "green" and num > 13)):
					add = False
					break

		if (add):
			total += game_id
	print(total)


