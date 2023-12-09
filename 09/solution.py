with open(0) as file:
    f = file.read().splitlines()

part1 = 0
part2 = 0

for l in f:
    results = []
    tmp1 = list(map(int, l.split()))
    results.append(tmp1)

    while any(tmp1):
        tmp2 = []
        for i, n in enumerate(tmp1[1:]):
            tmp2.append(n - tmp1[i])
        tmp1 = tmp2
        results.append(tmp1)

    num1 = 0
    num2 = 0

    for result in results[-2::-1]:
        num1 += result[-1]
        num2 = result[0] - num2

    part1 += num1
    part2 += num2

print(part1)
print(part2)
