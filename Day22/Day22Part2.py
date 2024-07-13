file = open('inputDay22.txt', 'r')
f = file.readlines()
test = """
Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%""".split('\n')


class Node:
    def __init__(self, size, used):
        self.size = size
        self.used = used

    def get_symbol(self):
        if self.used == 0:
            return '_'
        elif self.used > 200:
            return '#'
        else:
            return '.'


nodes = [[] for i in range(28)]
for i, line in enumerate(f):
    if i < 2:
        continue
    line_content = line.split()
    row = int(line_content[0].split('-')[2][1:])
    size = int(line_content[1][:-1])
    used = int(line_content[2][:-1])

    nodes[row].append(Node(size, used))


def display_nodes():
    for r, node_row in enumerate(nodes):
        for c, node in enumerate(node_row):
            if r == 0 and c == 0:
                print(f"({node.get_symbol()})", end='\t')
            elif r == 0 and c == len(node_row) - 1:
                print('G', end='\t')
            else:
                print(node.get_symbol(), end='\t')
        print()


display_nodes()
# figured it out by inspection from there
