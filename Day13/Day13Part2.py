
input_num = 1358
visited = []

def is_wall(x: int, y: int):
    return "{0:b}".format((x * x + 3 * x + 2 * x * y + y + y * y) + input_num).count('1') % 2 == 1


def display(x: int, y: int):
    for i in range(y):
        for j in range(x):
            if is_wall(j, i):
                print('#', end='')
            else:
                print('.', end='')
        print()


def add_coordinate(x: int, y: int, step: int, queue: list):
    if x >= 0 and y >= 0 and (x, y) not in visited and not is_wall(x, y):
        queue.append(((x, y), step + 1))
        visited.append((x, y))


def bfs(start: tuple[int, int], end: tuple[int, int]):
    queue = [(start, 0)]
    while True:
        coordinate = queue[0][0]
        step = queue[0][1]
        if step == 50:
            return len(visited)
        x = coordinate[0]
        y = coordinate[1]
        add_coordinate(x + 1, y, step, queue)
        add_coordinate(x - 1, y, step, queue)
        add_coordinate(x, y + 1, step, queue)
        add_coordinate(x, y - 1, step, queue)
        queue.pop(0)


display(10, 10)
print(bfs((1, 1), (31, 39)))
print(len(visited))
print(visited)