file = open('inputDay7.txt', 'r')
f = file.readlines()


def is_abba(group):
    return group[0] == group[3] and group[1] == group[2] and group[0] != group[1]


def scan_line(line):
    inside = False
    contains_key = False
    i = 0
    while i < len(line) - 3:
        group = line[i: i + 4]
        if '[' in group:
            inside = True
            i += 3
        elif ']' in group:
            inside = False
            i += 3

        if is_abba(group):
            if inside:
                return False
            else:
                contains_key = True
        #print(group)
        i += 1
    return contains_key


count = 0
for line in f:
    if scan_line(line):
        count += 1
print(count)