# --- Day 4: The Ideal Stocking Stuffer ---
# 
# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.
# 
# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
# 
# For example:
# 
# If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
# If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
# 
# --- Part Two ---
# 
# Now find one that starts with six zeroes.
# 
# 


# Part 1
# Puzzle input saved to file; read this in to a variable
with open('day04_input.txt', 'r') as myfile:
	secret = myfile.read().replace('\n','')

# Need hashlib in order to calculcate MD5 hash
import hashlib

have_answer = 0
test_dec = 0
part_1_ans = int()
part_2_ans = int()
while (have_answer == 0):
	# Build a combined string concatenating the decimal number to the secret
	combo_str = secret + str(test_dec)

	# Digest and return the hexadecimal hash
	hash_out = hashlib.md5(combo_str).hexdigest()

	# Test to see if the hash output starts with five zeroes
	if (hash_out[:5] == '00000' and not part_1_ans):
		part_1_ans = test_dec
		#print part_1_ans
	elif (hash_out[:6] == '000000' and not part_2_ans):
		part_2_ans = test_dec
		have_answer = 1
		#print part_2_ans
	test_dec += 1

print 'The answer for 5 leading zeroes (smallest integer) is ' + str(part_1_ans)
print 'The answer for 6 leading zeroes is ' + str(part_2_ans)


