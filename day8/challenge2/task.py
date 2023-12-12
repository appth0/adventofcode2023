import math
from functools import reduce

def parse_network(content):
    network = {}
    for line in content[2:]:
        s = line.split(" = ")
        network[s[0]] = [x.replace("(", "").replace(")", "").strip() for x in s[1].split(", ")]
    return network

def all_end_with_Z(nodes):
    nodes_end_with_Z = [x[-1] == "Z" for x in nodes]
    return reduce(lambda x, y: x and y, nodes_end_with_Z)


file = open('input.txt', 'r')
content = file.readlines()

network = parse_network(content)
instructions = content[0].strip()
current_nodes = [x for x in network.keys() if x[-1] == "A"]
steps = [0 for x in current_nodes]

for i, node in enumerate(current_nodes):
    while current_nodes[i][-1] != 'Z':
        for instruction in instructions:
            current_nodes[i] = network[current_nodes[i]][0 if instruction == 'L' else 1]
            steps[i] += 1

lcm = reduce(lambda x, y: math.lcm(x, y), steps)
print(lcm)
