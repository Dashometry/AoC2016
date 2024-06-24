from itertools import combinations
import copy

test = [["HM", "LM"], ["HG"], ["LG"], []]
inputP1 = [["SG", "SM", "PG", "PM"], ["TG", "RG", "RM", "CG", "CM"], ["TM"], []]
inputP2 = [["SG", "SM", "PG", "PM", "EG", "EM", "DG", "DM"], ["TG", "RG", "RM", "CG", "CM"], ["TM"], []]
floor = 0
visited = {}


def check_valid(floor_map):
    for floor in floor_map:
        generators = []
        microchips = []
        for item in floor:
            if 'G' in item:
                generators.append(item)
            else:
                microchips.append(item)
        if len(generators) > 0:
            for m in microchips:
                if (m[0] + 'G') not in generators:
                    return False
    return True


def display(floor_map, floor, step):
    print(f"step: {step}")
    for i in range(4):
        if floor == i:
            print(str(floor_map[i]) + ' <')
        else:
            print(floor_map[i])
    print()


def sort_floors(floor_map: list[list]):
    for floor in floor_map:
        floor.sort()


def to_string(floor_map):
    string = ''
    current_num = 0
    assigned_nums = {}
    for floor in floor_map:
        new_floor = []
        for item in floor:
            if item[0] in assigned_nums:
                new_floor.append(str(assigned_nums[item[0]]) + item[1])
            else:
                new_floor.append(str(current_num) + item[1])
                assigned_nums[item[0]] = current_num
                current_num += 1
        string = string + str(new_floor)
    return string


def at_top(floor_map):
    new_list = [[], [], [], []]
    for i in range(4):
        for item in floor_map[i]:
            new_list[3].append(item)
    return new_list


def add_to_queue(queue, floor_map, floor, step, group):
    final_copy = copy.deepcopy(floor_map)
    for item in group:
        final_copy[floor].append(item)

    sort_floors(final_copy)
    
    if check_valid(final_copy):
        queue.append((final_copy, floor))


def search_layer(queue, step, buffer_queue):
    copy1 = copy.deepcopy(queue[0][0])
    sort_floors(copy1)
    floor = queue[0][1]

    if to_string(copy1) + str(floor) in visited:
        queue.pop(0)
        return
    visited[to_string(copy1) + str(floor)] = step

    for i in range(1, 3):
        groups = list(combinations(copy1[floor], i))
        for group in groups:
            copy2 = copy.deepcopy(copy1)
            for item in group:
                #print(copy2[floor])
                copy2[floor].remove(item)

            new_floor = 0
            if floor + 1 < 4:
                new_floor = floor + 1
                add_to_queue(buffer_queue, copy2, new_floor, step, group)
            if floor - 1 >= 0:
                new_floor = floor - 1

                # don't move items down if floors below are empty
                count = 0
                for f in range(floor):
                    if len(copy2[f]) == 0:
                        count += 1
                if count == floor:
                    continue
                add_to_queue(buffer_queue, copy2, new_floor, step, group)
    queue.pop(0)


def bfs(floor_map: list[list], floor):
    step1 = 0
    queue1 = [(floor_map, floor)]
    buffer_queue1 = []
    top_floor = (at_top(floor_map))
    sort_floors(top_floor)
    target = top_floor

    while True:
        while len(queue1) > 0:
            search_layer(queue1, step1, buffer_queue1)

        for item in buffer_queue1:
            queue1.append(item)
        buffer_queue1.clear()
        step1 += 1
        print("step: " + str(step1))

        for state in queue1:
            if state[0] == target:
                return step1

        print(f'In queue: {len(queue1)}')


print(bfs(inputP1, 0))
