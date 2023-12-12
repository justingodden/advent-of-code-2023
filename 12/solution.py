with open(0) as file:
    f = file.read().splitlines()

cache = {}


def count(springs: str, groups: tuple[int, ...]) -> int:
    if springs == "":
        return 1 if groups == () else 0

    if groups == ():
        return 0 if "#" in springs else 1

    if (springs, groups) in cache:
        return cache[(springs, groups)]

    result = 0

    if springs[0] in ".?":
        result += count(springs[1:], groups)

    if springs[0] in "#?":
        if groups[0] <= len(springs):
            if "." not in springs[: groups[0]]:
                if groups[0] == len(springs) or springs[groups[0]] != "#":
                    result += count(springs[groups[0] + 1 :], groups[1:])

    cache[(springs, groups)] = result
    return result


total = 0

for l in f:
    springs, groups = l.split()
    groups = tuple(int(n) for n in groups.split(","))
    total += count(springs, groups)

print(total)

total = 0

for l in f:
    springs, groups = l.split()
    springs = "?".join([springs] * 5)
    groups = tuple(int(n) for n in groups.split(","))
    groups *= 5
    total += count(springs, groups)

print(total)
