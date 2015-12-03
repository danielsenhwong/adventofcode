with open("day01.txt", "r") as myfile:
	day01_input = myfile.read().replace('\n', '')

day01_list = list(day01_input)

floor = 0


for index in range(len(day01_list)):
	if index == 0:
		floor = 0
	if day01_list[index] == '(':
		floor += 1
	elif day01_list[index] == ')':
		floor -= 1

	# Part 2
	if floor == -1:
		print (index + 1)

print floor
