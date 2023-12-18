from heapq import heappush, heappop

with open(0) as file:
    f = [list(map(int, line)) for line in file.read().splitlines()]

seen = set()

pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    hl, j, i, dj, di, n = heappop(pq)

    if (j, i) == (len(f) - 1, len(f[0]) - 1) and n >= 4:
        print(hl)
        break

    if (j, i, dj, di, n) in seen:
        continue

    seen.add((j, i, dj, di, n))

    if n < 10 and (dj, di) != (0, 0):
        nj = j + dj
        ni = i + di
        if 0 <= nj < len(f) and 0 <= ni < len(f[0]):
            heappush(pq, (hl + f[nj][ni], nj, ni, dj, di, n + 1))

    if n >= 4 or (dj, di) == (0, 0):
        for ndj, ndi in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndj, ndi) != (dj, di) and (ndj, ndi) != (-dj, -di):
                nj = j + ndj
                ni = i + ndi
                if 0 <= nj < len(f) and 0 <= ni < len(f[0]):
                    heappush(pq, (hl + f[nj][ni], nj, ni, ndj, ndi, 1))
