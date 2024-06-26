file = open('inputDay20.txt', 'r')
f = file.readlines()
rn = range(9, 17)
print(rn.stop)
ranges = []

test = """5-8
0-2
4-7""".split('\n')


def join_ranges(rng: range):
    to_remove = []
    for item in ranges:
        start = item.start
        end = item.stop
        if rng.start < start < rng.stop < end:
            rng = range(rng.start, end)
            to_remove.append(item)
        elif start < rng.start < end < rng.stop:
            rng = range(start, rng.stop)
            to_remove.append(item)
        elif start <= rng.start and rng.stop <= end:
            return
        elif rng.start <= start and end <= rng.stop:
            to_remove.append(item)
        elif rng.stop == start or rng.stop + 1 == start:
            rng = range(rng.start, end)
            to_remove.append(item)
        elif end == rng.start or end + 1 == rng.start:
            rng = range(start, rng.stop)
            to_remove.append(item)
    for item in to_remove:
        ranges.remove(item)
    ranges.append(rng)


for line in f:
    line_contents = line.split('-')
    join_ranges(range(int(line_contents[0]), int(line_contents[1])))

for item in ranges:
    print(item)

allowed = 4294967296
for item in ranges:
    allowed -= (item.stop - item.start + 1)

print(allowed)