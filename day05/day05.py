# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# 
# Santa needs help figuring out which strings in his text file are naughty or
# nice.
# 
# A nice string is one with all of the following properties:
# 
# It contains at least three vowels (aeiou only), like aei, xazegov, or
# aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde
# (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of
# one of the other requirements.
# For example:
# 
# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...),
#  a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even
# though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# How many strings are nice?
# 
# 
# --- Part Two ---
# 
# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.
# 
# Now, a nice string is one with all of the following properties:
# 
# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
# For example:
# 
# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
# How many strings are nice under these new rules?

# Puzzle input saved to text file. Read this, strip the last newline break, and
# make a list with each line as a new list item
with open('day05_input.txt', 'r') as myfile:
	src = myfile.read().rstrip('\n').split('\n') 

# Use regular expression to check the strings
import re

# Keep track of the number of nice strings
nice_count = 0
nice_count_2 = 0

# Set up a list of invalid strings
invalid_str = ['ab', 'cd', 'pq', 'xy']

# Iterate through each item in the list
for test_str in src:
	# Count vowels and duplicates
	num_vowels = 0
	num_dup = 0

	# Set up flags
	has_invalid = 0

	# Iterate through each string
	for i in range(len(test_str)):
		# Set up previous letter tracking
		if i == 0:
			prev_letter = str()

		# Has at least one vowel
		if re.search('[aeiou]', test_str[i]):
			num_vowels += 1
		
		# Has duplicate
		if test_str[i] == prev_letter:
			num_dup += 1
		
		# Has invalid string
		if (prev_letter + test_str[i]) in invalid_str:
			has_invalid = 1

		# Keep track of previous letters
		prev_letter = test_str[i]

	if num_vowels >= 3 and num_dup >= 1 and not has_invalid:
		nice_count += 1	
	
print nice_count
