file = open('inputDay22.txt', 'r')
f = file.readlines()

nodes = []
for i, line in enumerate(f):
    if i < 2:
        continue
    line_content = line.split()
    nodes.append((int(line_content[2][:-1]), int(line_content[3][:-1])))

count = 0
for i, a in enumerate(nodes):
    for b in nodes[i + 1:]:
        if a[0] <= b[1] and a[0] != 0:
            count += 1
        if b[0] <= a[1] and b[0] != 0:
            count += 1

print(count)
