from collections import Counter

with open(0) as file:
    f = file.read()

d = {
    s.strip().split(" ")[0]: {"bid": int(s.strip().split(" ")[1])}
    for s in f.splitlines()
}

for k in d:
    v = list(Counter(k).values())
    # 5 of a kind
    if 5 in v:
        d[k]["type"] = 7
    # 4 of a kind
    elif 4 in v:
        d[k]["type"] = 6
    # full house or 3 of a kind
    elif 3 in v:
        if 2 in v:
            d[k]["type"] = 5
        else:
            d[k]["type"] = 4
    # 2 pair or 1 pair
    elif 2 in v:
        if v.count(2) == 2:
            d[k]["type"] = 3
        else:
            d[k]["type"] = 2
    # high card
    else:
        d[k]["type"] = 1

strengths = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

for k in d:
    d[k]["strength"] = []
    for ch in k:
        d[k]["strength"].append(strengths[ch])

d_sorted = sorted(
    d.items(),
    key=lambda item: (
        item[1]["type"],
        item[1]["strength"][0],
        item[1]["strength"][1],
        item[1]["strength"][2],
        item[1]["strength"][3],
        item[1]["strength"][4],
    ),
)

total = 0
for i, k in enumerate(d_sorted, 1):
    total += i * k[1]["bid"]

print(total)

for k in d:
    c = Counter(k)
    if "J" in c:
        J = c["J"]
        del c["J"]
    else:
        J = 0
    v = list(c.values())
    if J == 5:
        d[k]["type"] = 7
    # 5 of a kind
    elif 5 in v:
        d[k]["type"] = 7
    # 4 of a kind
    elif 4 in v:
        if J == 1:
            d[k]["type"] = 7
        else:
            d[k]["type"] = 6
    # full house or 3 of a kind
    elif 3 in v:
        if J == 2:
            d[k]["type"] = 7
        elif J == 1:
            d[k]["type"] = 6
        elif 2 in v:
            d[k]["type"] = 5
        else:
            d[k]["type"] = 4
    # 2 pair or 1 pair
    elif 2 in v:
        if J == 3:
            d[k]["type"] = 7
        elif J == 2:
            d[k]["type"] = 6
        elif J == 1:
            if v.count(2) == 2:
                d[k]["type"] = 5
            else:
                d[k]["type"] = 4
        elif v.count(2) == 2:
            d[k]["type"] = 3
        else:
            d[k]["type"] = 2
    # high card
    else:
        if J == 4:
            d[k]["type"] = 7
        elif J == 3:
            d[k]["type"] = 6
        elif J == 2:
            d[k]["type"] = 4
        elif J == 1:
            d[k]["type"] = 2
        else:
            d[k]["type"] = 1

strengths["J"] = 1

for k in d:
    d[k]["strength"] = []
    for ch in k:
        d[k]["strength"].append(strengths[ch])

d_sorted = sorted(
    d.items(),
    key=lambda item: (
        item[1]["type"],
        item[1]["strength"][0],
        item[1]["strength"][1],
        item[1]["strength"][2],
        item[1]["strength"][3],
        item[1]["strength"][4],
    ),
)

total = 0
for i, k in enumerate(d_sorted, 1):
    total += i * k[1]["bid"]

print(total)
