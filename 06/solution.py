with open(0) as file:
    f = file.read()

times, distances = f.splitlines()
times = [int(n) for n in times.split(":")[1].strip().split(" ") if n.isdigit()]
distances = [int(n) for n in distances.split(":")[1].strip().split(" ") if n.isdigit()]

total = 1
for i, t in enumerate(times):
    c = 0
    for s in range(1, t + 1):
        if s * (t - s) > distances[i]:
            c += 1
    total *= c

print(total)

time = int("".join([str(t) for t in times]))
distance = int("".join([str(d) for d in distances]))

c = 0
for s in range(1, time + 1):
    if s * (time - s) > distance:
        c += 1

print(c)
