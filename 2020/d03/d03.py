""" --- Day 3: Toboggan Trajectory ---
With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter? """

""" --- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes? """

# Initialize variables
d03_input = []

# Read the input, stripping newlines from the end of each line and saving each line as an item in a list
with open('d03/d03_input.txt') as f:
    d03_input = [(line.rstrip()) for line in f]
    f.close()
print(d03_input)
path = d03_input

num_trees = 0
i = 0
j = 0
num_trees_1_1 = 0
i_1_1 = 0
j_1_1 = 0
num_trees_1_5 = 0
i_1_5 = 0
j_1_5 = 0
num_trees_1_7 = 0
i_1_7 = 0
j_1_7 = 0
num_trees_2_1 = 0
i_2_1 = 0
j_2_1 = 0

for line in path:
    if i < len(path):
        if j >= len(line):
            j-=(len(line))
        if line[j] == '#':
            num_trees+=1
        print(i, len(line), j, line[j], num_trees)
        i+=1
        j+=3
    if i_1_1 < len(path):
        if j_1_1 >= len(line):
            j_1_1-=(len(line))
        if line[j_1_1] == '#':
            num_trees_1_1+=1
        print(i_1_1, len(line), j_1_1, line[j_1_1], num_trees_1_1)
        i_1_1+=1
        j_1_1+=1
    if i_1_5 < len(path):
        if j_1_5 >= len(line):
            j_1_5-=(len(line))
        if line[j_1_5] == '#':
            num_trees_1_5+=1
        print(i_1_5, len(line), j_1_5, line[j_1_5], num_trees_1_5)
        i_1_5+=1
        j_1_5+=5
    if i_1_7 < len(path):
        if j_1_7 >= len(line):
            j_1_7-=(len(line))
        if line[j_1_7] == '#':
            num_trees_1_7+=1
        print(i_1_7, len(line), j_1_7, line[j_1_7], num_trees_1_7)
        i_1_7+=1
        j_1_7+=7
    if i_2_1 < len(path):
        if (i_2_1) % 2 == 0:
            if j_2_1 >= len(line):
                j_2_1-=(len(line))
            if line[j_2_1] == '#':
                num_trees_2_1+=1
            print(i_2_1, len(line), j_2_1, line[j_2_1], num_trees_2_1)
        i_2_1+=1
        j_2_1+=1
print(num_trees, num_trees_1_1, num_trees_1_5, num_trees_1_7, num_trees_2_1)
print(num_trees * num_trees_1_1 * num_trees_1_5 * num_trees_1_7 * num_trees_2_1)

