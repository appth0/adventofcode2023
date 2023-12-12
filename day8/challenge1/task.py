
def parse_network(content):
    network = {}
    for line in content[2:]:
        s = line.split(" = ")
        network[s[0]] = [x.replace("(", "").replace(")", "").strip() for x in s[1].split(", ")]
    return network


file = open('input.txt', 'r')
content = file.readlines()

network = parse_network(content)
instructions = content[0].strip()
current_node = "AAA"

steps = 0
while current_node != "ZZZ":
    for instruction in instructions:
        current_node = network[current_node][0 if instruction == 'L' else 1]
        steps += 1

print(steps)
