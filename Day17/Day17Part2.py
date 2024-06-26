import hashlib

passcode = "edjrjqaa"
state = (0, 0, passcode)


def add_to_queue(queue, state, direction):
    x = state[0]
    y = state[1]
    code = state[2]
    if direction == 0:
        y -= 1
        code += 'U'
    elif direction == 1:
        y += 1
        code += 'D'
    elif direction == 2:
        x -= 1
        code += 'L'
    else:
        x += 1
        code += 'R'
    if -1 < x < 4 and -1 < y < 4:
        queue.append((x, y, code))


def bfs(state: tuple[int, int, str]):
    queue = [state]
    max = 0
    while len(queue) > 0:
        current = queue[0]
        code = current[2]
        if current[0] == 3 and current[1] == 3:
            max = len(code.replace(passcode, ''))
            queue.pop(0)
            print(max)
            continue

        hashcode = hashlib.md5(code.encode()).hexdigest()
        for i in range(4):
            if hashcode[i] in ['b', 'c', 'd', 'e', 'f']:
                add_to_queue(queue, current, i)
        queue.pop(0)

    return max


print(bfs(state))
