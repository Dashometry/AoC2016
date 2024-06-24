file = open('inputDay8.txt', 'r')
f = file.readlines()
grid = []
test = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1""".split("\n")


def init_grid(rows, cols):
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append('.')
        grid.append(row)


def display_grid():
    for row in grid:
        for item in row:
            print(item, end='')
        print()


def rect(width, height):
    for i in range(height):
        for j in range(width):
            grid[i][j] = '#'


def rotate_row(y: int, num: int):
    grid[y] = grid[y][-num:] + grid[y][: -num]


def rotate_col(x: int, num: int):
    new_col = []
    for i in range(len(grid)):
        new_col.append(grid[i][x])

    for i in range(len(grid) - num):
        new_col[i + num] = grid[i][x]
    for i in range(num):
        new_col[i] = grid[len(grid) - num + i][x]

    for i in range(len(grid)):
        grid[i][x] = new_col[i]


init_grid(6, 50)
#rect(5, 3)
#rotate_row(0, 2)
#rotate_col(3, 2)
#display_grid()

for line in f:
    line_list = line.split(' ')
    if line_list[0] == 'rect':
        rect(int(line_list[1].split('x')[0]), int(line_list[1].split('x')[1]))
    elif line_list[1] == 'row':
        rotate_row(int(line_list[2][2:]), int(line_list[4]))
    else:
        rotate_col(int(line_list[2][2:]), int(line_list[4]))

display_grid()

count = 0
for row in grid:
    for item in row:
        if item == '#':
            count += 1
print(count)
