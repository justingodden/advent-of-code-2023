import re

with open(0) as file:
    f = file.read().splitlines()

c = 0

for l in f:
    l = re.sub("[^\d+]", "", l)
    try:
        c += int(l[0] + l[-1])
    except Exception as e:
        pass

print(c)

lookup = {
    "oneight": "18",
    "twone": "21",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "nineight": "98",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

c = 0

for l in f:
    for k in lookup:
        l = l.replace(k, lookup[k])
    l = re.sub("[^\d+]", "", l)
    c += int(l[0] + l[-1])

print(c)
