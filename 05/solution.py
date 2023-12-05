from multiprocessing import Pool
import time


with open(0) as file:
    f = file.read()

seeds = [int(n) for n in f.splitlines()[0].split(": ")[1].split(" ")]

f = f.rstrip().split("\n\n")[1:]
mappings = []
for block in f:
    mapping = []
    for s in block.split(":\n")[1].split("\n"):
        tmp = []
        for n in s.split(" "):
            tmp.append(int(n))
        mapping.append(tmp)
    mappings.append(mapping)

min_loc = float("inf")

for seed in seeds:
    val = seed
    for mapping in mappings:
        for m in mapping:
            if m[1] <= val and val < m[1] + m[2]:
                val = m[0] + val - m[1]
                break
    if val < min_loc:
        min_loc = val

print(min_loc)


def func(seed):
    val = seed
    for mapping in mappings:
        for m in mapping:
            if m[1] <= val and val < m[1] + m[2]:
                val = m[0] + val - m[1]
                break

    return val


min_loc = float("inf")

total_start_t = time.perf_counter()

for i in range(0, len(seeds), 2):
    print(
        f"Seed set: {(i // 2) + 1}/{len(seeds) // 2} - Total iterations: {seeds[i + 1]:.2E}"
    )
    start_t = time.perf_counter()
    with Pool() as executor:
        future = executor.imap_unordered(
            func, range(seeds[i], seeds[i] + seeds[i + 1]), chunksize=20000
        )
        for val in future:
            if val < min_loc:
                min_loc = val
    end_t = time.perf_counter()
    print(f"Duration: {(end_t - start_t):.2f}s")

total_end_t = time.perf_counter()
print(f"Total Duration: {(total_end_t - total_start_t):.2f}s")

print(min_loc)
