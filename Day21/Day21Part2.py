file = open('inputDay21.txt', 'r')
f = file.readlines()
f.reverse()
test = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d""".split('\n')
test.reverse()


def set_char(string: str, index, char):
    return string[:index] + char + string[index + 1:]


def swap_positions(string: str, x, y):
    temp = string[y]
    string = set_char(string, y, string[x])
    string = set_char(string, x, temp)
    return string


def swap_letters(string: str, x, y):
    x_index = string.index(x)
    y_index = string.index(y)
    string = set_char(string, x_index, y)
    string = set_char(string, y_index, x)
    return string


def rotate_left(string: str, steps):
    steps = steps % len(string)
    return string[steps:] + string[: steps]


def rotate_right(string: str, steps):
    steps = steps % len(string)
    return string[-steps:] + string[:-steps]


def rotate_based_on(string: str, letter):
    index = string.index(letter)
    if index % 2 == 1:
        string = rotate_left(string, int((index + 1) / 2))
    else:
        if index == 0:
            string = rotate_left(string, 1)
        else:
            string = rotate_right(string, int((6 - index) / 2))
    return string


def reverse_positions(string: str, x, y):
    reverse = string[x: y+1]
    reverse = reverse[::-1]
    return string[:x] + reverse + string[y + 1:]


def move_positions(string: str, y, x):
    temp = string[x]
    string = string.replace(temp, '')
    string = string[:y] + temp + string[y:]
    return string


print("abcdefgh".index('a'))

string = "fbgdceah"

for line in f:
    print(string)
    info = line.split(' ')

    if info[0] == 'swap':
        if info[1] == 'position':
            string = swap_positions(string, int(info[2]), int(info[5].strip()))
        else:
            string = swap_letters(string, info[2], info[5].strip())
    elif info[0] == 'rotate':
        if len(info) > 4:
            string = rotate_based_on(string, info[6].strip())
        elif info[1] == 'right':
            string = rotate_left(string, int(info[2]))
        else:
            string = rotate_right(string, int(info[2]))
    elif info[0] == 'reverse':
        string = reverse_positions(string, int(info[2]), int(info[4].strip()))
    else:
        string = move_positions(string, int(info[2]), int(info[5].strip()))

print(string)