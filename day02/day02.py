# --- Day 2: I Was Told There Would Be No Math ---
#
# The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.
#
# Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.
#
# For example:
#
# A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
# A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
# All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

# Puzzle inpu was saved to a text file.
# Read this in, but each new line (measurement) is a new list element.
# Remember to trim off the trailing newline break at the end.
with open("day02_input.txt", "r") as myfile:
	src_data = myfile.read().rstrip('\n')
	data_list = src_data.split('\n')

# Need prod() function similar to sum() function in order to caluclate product of list
from operator import mul
def prod(iterable):
	return reduce(mul, iterable, 1)

# For each list element, split the expression of measurements into individual integers, and calculate
for index in range(len(data_list)):
	# initialize the empty list
	if index == 0:
		data_calc = []
	# split each set of measurements
	for package in data_list[index]:
		meas = [int(n) for n in data_list[index].split('x')]	
	# calculate the surface area + slack for each gift individually, and load into a new list
	calc_area = (2 * (meas[0]*meas[1] + meas[1]*meas[2] + meas[2]*meas[0])) + (prod(meas) / max(meas))
	data_calc.append(calc_area)

# sum all calculated areas
day02_answer = sum(data_calc)

print 'Total gift wrap needed in square feet: ' + str(day02_answer)


# Part 2

# The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.
#
# The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.
#
# For example:
#
# A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
# A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
# How many total feet of ribbon should they order?
#


for index in range(len(data_list)):
        # initialize the empty list
        if index == 0:
                data_calc = []
        # split each set of measurements
        for package in data_list[index]:
                meas = [int(n) for n in data_list[index].split('x')]
	# Calculate ribbon length needed for each gift individually, and load into a new list
        calc_ribbon = (2 * sum(sorted(meas)[:2])) + prod(meas)
        data_calc.append(calc_ribbon)

ribbon_total = sum(data_calc)

print 'Total ribbon length needed, in feet: ' + str(ribbon_total)
