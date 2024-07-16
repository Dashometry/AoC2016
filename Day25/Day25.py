file = open('inputDay25.txt', 'r')
f = file.readlines()

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
output = []
i = 0
count = 0
start_value = 0
while i < len(f):
    if i == 29:  # this is when the instructions loop again, thus the output starts to loop as well
        print(start_value)
        if output == [0, 1] * (len(output) // 2):
            print(output)
            break
        else:
            output = []
            start_value += 1
            registers = {'a': start_value, 'b': 0, 'c': 0, 'd': 0}
            i = 0

    line = f[i].strip().split(' ')
    if line[0] == 'cpy':
        if not line[2].lstrip('-').isdigit():
            if line[1].lstrip('-').isdigit():
                registers[line[2]] = int(line[1])
            else:
                registers[line[2]] = registers[line[1]]
            # print(f"copying {line[1]} to register {line[2]}")
    elif line[0] == 'inc':
        if not line[1].lstrip('-').isdigit():
            registers[line[1]] += 1
            # print(f"increment register {line[1]}")
    elif line[0] == 'dec':
        if not line[1].lstrip('-').isdigit():
            registers[line[1]] -= 1
            # print(f"decrement register {line[1]}")
    elif line[0] == 'jnz':
        if line[1].isdigit():
            value = int(line[1])
        else:
            value = registers[line[1]]
        if value != 0:
            if line[2].lstrip('-').isdigit():
                jump = int(line[2])
            else:
                jump = registers[line[2]]
            i += jump - 1
            # print(f"jump {line[2]} since value is {value}")
        else:
            pass
            # print("no jump")
    elif line[0] == 'out':
        output.append(int(line[1]) if line[1].lstrip('-').isdigit() else registers[line[1]])
        # print(f"output: {output}")
        if len(output) > 100:
            break

    i += 1
    count += 1
