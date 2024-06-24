file = open('inputDay6.txt', 'r')
f = file.readlines()
columns = []
test = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""".split('\n')


def init_columns(rows):
    length = len(rows[0].strip())
    print(length)

    for i in range(length):
        columns.append([])

    for line in rows:
        for i in range(length):
            columns[i].append(line[i])

    for col in columns:
        for char in col:
            print(char, end=", ")
        print()


def find_lowest_char(column: list[str]):
    appeared = []
    lowest_char = ''
    for char in column:
        if char not in appeared:
            appeared.append(char)
            if lowest_char == '' or column.count(char) < column.count(lowest_char):
                lowest_char = char
    return lowest_char


init_columns(f)
message = ''
for col in columns:
    message = message + find_lowest_char(col)

print(message)