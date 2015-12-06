# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# 
# Santa is delivering presents to an infinite two-dimensional grid of houses.
# 
# He begins by delivering a present to the house at his starting location, and
# then an elf at the North Pole calls him via radio and tells him where to move
# next. Moves are always exactly one house to the north (^), south (v), east
# (>), or west (<). After each move, he delivers another present to the house at
# his new location.
# 
# However, the elf back at the north pole has had a little too much eggnog, and
# so his directions are a little off, and Santa ends up visiting some houses
# more than once. How many houses receive at least one present?
# 
# For example:
# 
# 	> delivers presents to 2 houses: one at the starting location, and one
# 	to the east.  ^>v< delivers presents to 4 houses in a square, including
# 	twice to the house at his starting/ending location.  ^v^v^v^v^v delivers
# 	a bunch of presents to some very lucky children at only 2 houses.
# 
# --- Part Two ---
# 
# The next year, to speed up the process, Santa creates a robot version of
# himself, Robo-Santa, to deliver presents with him.
# 
# Santa and Robo-Santa start at the same location (delivering two presents to
# the same starting house), then take turns moving based on instructions from
# the elf, who is eggnoggedly reading from the same script as the previous year.
# 
# This year, how many houses receive at least one present?
# 
# For example:
# 
# 	^v delivers presents to 3 houses, because Santa goes north, and then
# 	Robo-Santa goes south.  ^>v< now delivers presents to 3 houses, and
# 	Santa and Robo-Santa end up back where they started.  ^v^v^v^v^v now
# 	delivers presents to 11 houses, with Santa going one direction and
# 	Robo-Santa going the other.
# 




# Part 1
# Puzzle input saved to file, read in and strip newline breaks
with open('day03.txt', 'r') as myfile:
	input3 = myfile.read().replace('\n','')

# ^ north
# v south
# > east
# < west

# How many houses get at least one present?
# Possible solution:
# Locations are all points on 2D Cartesian coordinate plane, so:
#	- set up list, e.g. coords[], with two integers, e.g. x and y
#	- walk through all given directions in input
#	- for each step, in/decrement coords[] x or y as appropriate.
#		e.g. ^ = +1,0, v = -1, 0, > = 0,+1, < = 0,-1
#	- count duplicates in coords[]

# Convert input to list of single characters
dirs = list(input3)

# Keep track of coordinates as a list of tuples
coords = [(0,0)]

# Iterate through list of directions
# Start at origin (0,0) and read the next direction from dirs[].  Take the
# previous point's coordinates as a tuple, and increment just the  appropriate
# part.  Save the new coordinate as the next point, then add it to the list of
# visited homes.
for index in range(len(dirs)):
	if dirs[index] == '^':
		next_point = tuple((coords[index][0] + 1,
				coords[index][1]))
	elif dirs[index] == 'v':
		next_point = tuple((coords[index][0] - 1,
				coords[index][1]))
	elif dirs[index] == '>':
		next_point = tuple((coords[index][0],
				coords[index][1] + 1))
	elif dirs[index] == '<':
		next_point = tuple((coords[index][0],
				coords[index][1] - 1))
	coords.append(next_point)

# Count duplicates Tuples can be hashed and used as keys in a dictionary {}, so
# do that and  keep track of which homes we've visited. A dictionary is used
# because it stores key-value pairs, and we want to count how many times we
# visit each house, identified by its coordinates as a key.
visited = {}
for house in coords:
	if house in visited:
		visited[house] += 1
	else:
		visited[house] = 1

# Now count; originally designed to count repeats
visits = 0
for key, value in visited.items():
	if value >= 1:
		visits += 1

print 'Number of houses receiving at least one present: ' + str(visits)


# Part Two
# Keep track of coordinates with two different lists Santa takes coordinates
# with odd indices, Robo-Santa takes coordinates with even


santa_coords = [(0,0)]
robo_coords = [(0,0)]

for index in range(len(dirs)):
	# If even, Robo-Santa will follow the directions, so pull its last
	# coordinates. Otherwise, Santa.
	if index % 2 == 0: # Robo-Santa
		prev_point = robo_coords[-1]
	elif index % 2 == 1: # Santa
		prev_point = santa_coords[-1]
	
	# Same direction mapping as last time
	if dirs[index] == '^':
		next_point = tuple((prev_point[0] + 1,
			prev_point[1]))
	elif dirs[index] == 'v':
		next_point = tuple((prev_point[0] - 1,
			prev_point[1]))
	elif dirs[index] == '>':
		next_point = tuple((prev_point[0],
			prev_point[1] + 1))
	elif dirs[index] == '<':
		next_point = tuple((prev_point[0],
			prev_point[1] - 1))

	# Save the new coordinate to the appropriate individual
	if index % 2 == 0:
		robo_coords.append(next_point)
	elif index % 2 == 1:
		santa_coords.append(next_point)

# New dictionary so we only count unique visits
visited_part2 = {}
coords = santa_coords + robo_coords
for house in coords:
	if house in visited_part2:
		visited_part2[house] += 1
	else:
		visited_part2[house] = 1

# Return the result
print 'Houses receiving at least one present in part 2: ' + str(len(visited_part2))
