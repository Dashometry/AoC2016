file = open('inputDay23.txt', 'r')
f = file.readlines()
test = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a""".split('\n')

registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}

i = 0
while i < len(f):
    line = f[i].strip().split(' ')
    if line[0] == 'cpy':
        if not line[2].lstrip('-').isdigit():
            if line[1].lstrip('-').isdigit():
                registers[line[2]] = int(line[1])
            else:
                registers[line[2]] = registers[line[1]]
            print(f"copying {line[1]} to register {line[2]}")
    elif line[0] == 'inc':
        if not line[1].lstrip('-').isdigit():
            registers[line[1]] += 1
            print(f"increment register {line[1]}")
    elif line[0] == 'dec':
        if not line[1].lstrip('-').isdigit():
            registers[line[1]] -= 1
            print(f"decrement register {line[1]}")
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
            print(f"jump {line[2]} since value is {value}")
        else:
            print("no jump")
    elif line[0] == 'tgl':
        away = int(registers[line[1]])
        if 0 <= i + away < len(f):
            target_line = f[i + away].split()
            if len(target_line) == 2:  # one-argument instruction
                if target_line[0] == "inc":
                    f[i + away] = "dec" + f[i + away][3:]
                else:
                    f[i + away] = "inc" + f[i + away][3:]
            else:  # two_argument instruction
                if target_line[0] == "jnz":
                    f[i + away] = "cpy" + f[i + away][3:]
                else:
                    f[i + away] = "jnz" + f[i + away][3:]

    i += 1

    print(registers)
    print(f'{i}, {len(f)}')

print(registers['a'])
