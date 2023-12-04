with open(0) as file:
    f = file.read().splitlines()

# f = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split(
#     "\n"
# )

score = 0

for l in f:
    l = l.replace("  ", " ")
    winning = [int(n) for n in l.split(" |")[0].split(": ")[1].split(" ")]
    ours = [int(n) for n in l.split("| ")[1].split(" ")]
    points = 0
    for n in winning:
        if n in ours:
            if points == 0:
                points = 1
            else:
                points *= 2
    score += points

print(score)

scratchcards = {n: 1 for n in range(1, len(f) + 1)}

for l in f:
    l = l.replace("   ", " ")
    l = l.replace("  ", " ")
    card_num = int(l.split(":")[0].split(" ")[1])
    winning = [int(n) for n in l.split(" |")[0].split(": ")[1].split(" ")]
    ours = [int(n) for n in l.split("| ")[1].split(" ")]

    for _ in range(scratchcards[card_num]):
        num_winning = 0
        for n in winning:
            if n in ours:
                num_winning += 1
        for n in range(num_winning):
            scratchcards[card_num + n + 1] += 1

total = 0
for k in scratchcards:
    total += scratchcards[k]

print(total)
