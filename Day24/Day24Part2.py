import math
from collections import deque

file = open('inputDay24.txt', 'r')
f = file.readlines()
grid = []
num_locations = {}
shortest_dist_pairs = {}
test = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########""".split('\n')


def parse_grid():
    for line in f:
        line = line.strip()
        grid.append([])
        for char in line:
            grid[-1].append(char)


def display_grid():
    for row in grid:
        for char in row:
            print(char, end='')
        print()


def get_num_locations():
    def iterate(n):
        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if str(n) == char:
                    num_locations[n] = (i, j)
                    return True
        return False

    num = 0
    while True:
        if not iterate(num):
            break
        num += 1


def get_shortest_dist_pairs():
    nums = len(num_locations)
    for i in range(0, nums):
        for j in range(i + 1, nums):
            steps = bfs(num_locations[i], num_locations[j])
            key = str(i) + str(j)
            shortest_dist_pairs[key] = steps


def bfs(start, target):
    visited = set()
    queue = deque()
    queue.append((start, 0))
    while queue:
        pos, step = queue.popleft()
        row, col = pos
        if pos == target:
            return step
        elif not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] == '#' or pos in visited:
            continue

        visited.add(pos)
        queue.append(((row + 1, col), step + 1))
        queue.append(((row - 1, col), step + 1))
        queue.append(((row, col + 1), step + 1))
        queue.append(((row, col - 1), step + 1))


min_steps = math.inf


def find_min_steps(curr_num, steps, remaining):
    global min_steps
    if steps >= min_steps:
        return
    if len(remaining) == 0:
        key = '0' + str(curr_num)
        steps += shortest_dist_pairs[key]
        if steps < min_steps:
            min_steps = steps
        return

    for num in remaining:
        remaining_copy = {i for i in remaining}
        remaining_copy.remove(num)
        key = "".join(sorted([str(curr_num), str(num)]))
        new_steps = steps + shortest_dist_pairs[key]
        find_min_steps(num, new_steps, remaining_copy)
    return


parse_grid()
get_num_locations()
get_shortest_dist_pairs()

find_min_steps(0, 0, {i for i in num_locations if i != 0})
print(min_steps)
