import random

keep_rolling = True

while keep_rolling:
	inp = input("Keep Rolling? [Y/N]")       

	if inp != "N":
		print(random.randint(1,6))

	else:
		keep_rolling = False