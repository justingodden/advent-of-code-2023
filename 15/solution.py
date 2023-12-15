with open(0) as file:
    f = file.read().strip()
f = f.split(",")


def HASH(ch: str, curr: int) -> int:
    curr += ord(ch)
    curr *= 17
    curr %= 256
    return curr


total = 0
for l in f:
    res = 0
    for ch in l:
        res = HASH(ch, res)
    total += res

print(total)

boxes = [[] for _ in range(256)]

for l in f:
    if "=" in l:
        s, n = l.split("=")
        n = int(n)
    else:
        s = l.replace("-", "")
        n = None

    box_id = 0
    for ch in s:
        box_id = HASH(ch, box_id)

    if n is not None:
        idx = None
        for i, d in enumerate(boxes[box_id]):
            if s in d:
                idx = i
        if idx is not None:
            boxes[box_id][idx] = {s: n}
        else:
            boxes[box_id].append({s: n})
    else:
        boxes[box_id] = [d for d in boxes[box_id] if s not in d]

power = 0
for box_num, box in enumerate(boxes, 1):
    for slot, d in enumerate(box, 1):
        power += box_num * slot * list(d.values())[0]

print(power)
