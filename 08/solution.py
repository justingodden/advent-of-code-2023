from collections import defaultdict
import math

with open(0) as file:
    f = file.read()

instructions, node_block = f.split("\n\n")

nodes = defaultdict(dict)

for line in node_block.strip().split("\n"):
    a, b = line.split(" = ")
    b = b.replace("(", "").replace(")", "")
    l, r = b.split(", ")
    nodes[a]["L"] = l
    nodes[a]["R"] = r

steps = 0
current = "AAA"

while current != "ZZZ":
    for ch in instructions:
        current = nodes[current][ch]
        steps += 1
        if current == "ZZZ":
            break

print(steps)

starting_points = []
for k in nodes:
    if k[2] == "A":
        starting_points.append(k)

steps_to_z = [None for _ in range(len(starting_points))]

for i, current in enumerate(starting_points):
    steps = 0
    while current[2] != "Z":
        for ch in instructions:
            current = nodes[current][ch]
            steps += 1
            if current[2] == "Z":
                steps_to_z[i] = steps
                break

print(math.lcm(*steps_to_z))
