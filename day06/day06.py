# --- Day 6: Probably a Fire Hazard ---
# 
# Because your neighbors keep defeating you in the holiday house decorating
# contest year after year, you've decided to deploy one million lights in a
# 1000x1000 grid.
# 
# Furthermore, because you've been especially nice this year, Santa has mailed you
# instructions on how to display the ideal lighting configuration.
# 
# Lights in your grid are numbered from 0 to 999 in each direction; the lights at
# each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include
# whether to turn on, turn off, or toggle various inclusive ranges given as
# coordinate pairs. Each coordinate pair represents opposite corners of a
# rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to
# 9 lights in a 3x3 square. The lights all start turned off.
# 
# To defeat your neighbors this year, all you have to do is set up your lights by
# doing the instructions Santa sent you in order.
# 
# For example:
# 
# 	turn on 0,0 through 999,999 would turn on (or leave on) every light.
# 	toggle 0,0 through 999,0 would toggle the first line of 1000 lights,
# 	turning off the ones that were on, and turning on the ones that were
# 	off.  turn off 499,499 through 500,500 would turn off (or leave off) the
# 	middle four lights.  After following the instructions, how many lights
# 	are lit?
# --- Part Two ---
# 
# You just finish implementing your winning light pattern when you realize you
# mistranslated Santa's message from Ancient Nordic Elvish.
# 
# The light grid you bought actually has individual brightness controls; each
# light can have a brightness of zero or more. The lights all start at zero.
# 
# The phrase turn on actually means that you should increase the brightness of
# those lights by 1.
# 
# The phrase turn off actually means that you should decrease the brightness of
# those lights by 1, to a minimum of zero.
# 
# The phrase toggle actually means that you should increase the brightness of
# those lights by 2.
# 
# What is the total brightness of all lights combined after following Santa's
# instructions?
# 
# For example:
# 
# 	turn on 0,0 through 0,0 would increase the total brightness by 1.
# 	toggle 0,0 through 999,999 would increase the total brightness by
# 	2000000.
# 

# Part 1
with open('day06_input.txt', 'r') as myfile:
	src = myfile.read().splitlines()

# Need regular expressions again
import re

# Also need numpy
import numpy

# Initialize array of states for all lights
lights = numpy.zeros((10000,10000), bool)
lights_2 = numpy.zeros((10000,10000), int)

for inst in src:
	detail = re.match(r'([a-z]+\s*[a-z]+)\s([0-9]+),([0-9]+)\s([a-z]+)\s([0-9]+),([0-9]+)', inst).groups()
	# detail[0] = action
	# detail[1] = start x
	# detail[2] = start y
	# detail[3] = through
	# detail[4] = end x
	# detail[5] = end y

	x_start = int(detail[1])
	x_end = int(detail[4]) + 1 # + 1 because inclusive
	y_start = int(detail[2])
	y_end = int(detail[5]) + 1 # + 1 because inclusive

	if detail[0] == 'turn on':
		lights[x_start:x_end, y_start:y_end] = True
		lights_2[x_start:x_end, y_start:y_end] += 1
	elif detail[0] == 'toggle':
		lights[x_start:x_end, y_start:y_end] = ~lights[x_start:x_end,y_start:y_end] # ~ Inverts values
		lights_2[x_start:x_end, y_start:y_end] += 2
	elif detail[0] == 'turn off':
		lights[x_start:x_end, y_start:y_end] = False
		lights_2[x_start:x_end, y_start:y_end] -= 1 
		lights_2[lights_2 < 0] = 0 # Do not allow negatives

lights_on = sum(sum(lights))
brightness = sum(sum(lights_2))
print 'Lights on: ' + str(lights_on)
print 'Total brightness: ' + str(brightness)
