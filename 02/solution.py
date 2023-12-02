import re
import math

with open(0) as file:
    f = file.read().splitlines()

limits = {"red": 12, "green": 13, "blue": 14}
count = 0

for line in f:
    left_part = line.split(":")[0]
    right_part = line.split(":")[1]
    id = int(re.sub("[^0-9]", "", left_part))

    subsets = right_part.split(";")

    passed = True

    for subset in subsets:
        colours = subset.split(",")

        for colour in colours:
            word = re.sub("[^a-z]", "", colour)
            num = int(re.sub("[^0-9]", "", colour))

            if num > limits[word]:
                passed = False

    if passed:
        count += id

print(count)

power = 0

for line in f:
    right_part = line.split(":")[1]
    subsets = right_part.split(";")
    mins = {"red": 0, "green": 0, "blue": 0}

    for subset in subsets:
        colours = subset.split(",")

        for colour in colours:
            word = re.sub("[^a-z]", "", colour)
            num = int(re.sub("[^0-9]", "", colour))

            mins[word] = max(mins[word], num)

    power += math.prod([mins[k] for k in mins])

print(power)
