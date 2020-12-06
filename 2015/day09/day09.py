""" --- Day 9: All in a Single Night ---
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route? """

import re
import sys
from itertools import permutations

data = []
places = set()
distances = dict()

for line in open('2015/day09/day09_input.txt'):
    data.append([x.rstrip() for x in re.split(' to | = ', line)])

    # solution from elsewhere, very interesting way of importing data
    # i've never used the set datatype before
    (source, _, dest, _, distance) = line.split()
    places.add(source)
    places.add(dest)
    # also never used setdefault before to set up a dictionary
    # super interesting, sets up a nested dict off the top
    # each location is searched in the distances dict, and if it doesn't exist, a nested dict is created with that location as the key
    # then within the nested dict, the name of another location and the distance to it are the key, value pair
    distances.setdefault(source, dict())[dest] = int(distance)
    distances.setdefault(dest, dict())[source] = int(distance)

# solution from elsewhere
# return the largest positive integer supported by the platform
shortest = sys.maxsize
# initialize
longest = 0
# iterate through the list of permutations of places (all the different orders you could go)
# set up a temporary variable dist to figure out the distance with a lambda function, which has two variables x and y in a function to look up the distance in the distances dict, items[:-1] and items[1:] are the values passed to x and y. these are everything except the last location, and everything but the first location to come up with source-dest pairs to look up distances
# min max to find shortest and longest
for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print("shortest: %d" % (shortest))
print("longest: %d" % (longest))