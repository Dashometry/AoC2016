file = open('inputDay7.txt', 'r')
f = file.readlines()


def is_aba(group):
    return group[0] == group[2] and group[0] != group[1]


def get_corresponding(group):
    return group[1] + group[0] + group[1]


def scan_line(line):
    outside_groups = []
    inside_groups = []
    inside = False
    contains_key = False
    i = 0
    while i < len(line) - 2:
        group = line[i: i + 3]
        if '[' in group:
            inside = True
            i += 2
        elif ']' in group:
            inside = False
            i += 2

        if is_aba(group):
            if inside:
                inside_groups.append(group)
            else:
                outside_groups.append(group)
        #print(group)
        i += 1

    for group in inside_groups:
        if get_corresponding(group) in outside_groups:
            return True
    return False


count = 0
for line in f:
    if scan_line(line):
        count += 1
print(count)
