""" --- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a? """

""" --- Part Two ---
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a? """

import pprint
pp = pprint.PrettyPrinter(indent=4)

with open('2015/day07/day07_input.txt', 'r') as myfile:
    src = myfile.read().rstrip('\n').split('\n')
    myfile.close()

circuit_list = []

for line in src:
    # print(line)
    # Break the line apart to get the connection information
    l = line.split(" -> ")
    # Convert words to bitwise operators
    l[0] = l[0].replace("AND", "&")
    l[0] = l[0].replace("OR", "|")
    l[0] = l[0].replace("NOT", "~")
    l[0] = l[0].replace("LSHIFT", "<<")
    l[0] = l[0].replace("RSHIFT", ">>")
    l[0] = l[0].split(" ")
    # make a tuple out of the list of parts of the line
    t = tuple(l)
    # Then make a list out of that so we can put it into a dictionary
    circuit_list.append(t)
    # print(l)

# make a dictionary that has connections as keys and the inputs to them as the values
circuit_dict = dict(map(reversed, circuit_list))

result_dict = {}

# pull out the direct inputs first
for k, v in circuit_dict.items():
    if len(v) == 1:
        if v[0].isdigit():
            # these are direct inputs
            result_dict[k] = int(v[0])

# find the direct inputs and calculate their dependents, and repeat until result_dict has solved everything
while len(result_dict) < len(circuit_dict):
    for k, v in circuit_dict.items():
        to_eval = []
        tmp_str = ''
        for x in v:
            # Iterate through the list of connection statement parts
            if x in result_dict.keys():
                #print(v)
                tmp_str += str(result_dict[x])
                to_eval.append(True)
            elif x.isalpha():
                tmp_str += x
                to_eval.append(False)
            else: 
                tmp_str += x
        # If we have an existing input, then let's calculate the connection
        if not False in to_eval:
            #print(tmp_str)
            out = eval(tmp_str)
            result_dict[k] = out

pp.pprint(circuit_dict)
pp.pprint(result_dict)
print(result_dict['a'])

circuit_dict_2 = circuit_dict
circuit_dict_2['b'] = [str(result_dict['a'])]

result_dict_2 = {}
    
# pull out the direct inputs first
for k, v in circuit_dict_2.items():
    if len(v) == 1:
        if v[0].isdigit():
            # these are direct inputs
            result_dict_2[k] = int(v[0])

# find the direct inputs and calculate their dependents, and repeat until result_dict has solved everything
while len(result_dict_2) < len(circuit_dict_2):
    for k, v in circuit_dict_2.items():
        to_eval = []
        tmp_str = ''
        for x in v:
            # Iterate through the list of connection statement parts
            if x in result_dict_2.keys():
                #print(v)
                tmp_str += str(result_dict_2[x])
                to_eval.append(True)
            elif x.isalpha():
                tmp_str += x
                to_eval.append(False)
            else: 
                tmp_str += x
        # If we have an existing input, then let's calculate the connection
        if not False in to_eval:
            #print(tmp_str)
            out = eval(tmp_str)
            result_dict_2[k] = out

pp.pprint(circuit_dict_2)
pp.pprint(result_dict_2)
print(result_dict_2['a'])