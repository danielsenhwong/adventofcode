""" --- Day 10: Elves Look, Elves Say ---
Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

For example:

1 becomes 11 (1 copy of digit 1).
11 becomes 21 (2 copies of digit 1).
21 becomes 1211 (one 2 followed by one 1).
1211 becomes 111221 (one 1, one 2, and two 1s).
111221 becomes 312211 (three 1s, two 2s, and one 1).
Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

Your puzzle input is 3113322113. """

src = '3113322113'

# Terribly slow
""" e_src = enumerate(src)
prev_v = ''
next_src = ''
n = 0
num_loops = 40
r = 0
while r < num_loops: 
    for i, v in e_src:
        # print(v, prev_v, n, next_src)
        if v == prev_v:
            n+=1
            prev_v = v
        else:
            if n > 0:
                next_src+=str(n)
                next_src+=str(prev_v)
            n = 1
            prev_v = v
    next_src+=str(n)
    next_src+=str(prev_v)
    # print(src, next_src)
    e_src = enumerate(next_src)
    r+=1
    # print(r)
        
len(next_src) """

# Solution from elsewhere
from itertools import groupby

def look_and_say(input_string, num_iterations):
    for i in range(num_iterations):
        input_string = ''.join([str(len(list(g))) + str(k) for k, g in groupby(input_string)])
    return input_string

len(look_and_say(src, 40))
len(look_and_say(src, 50))