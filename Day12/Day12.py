file = open('inputDay12.txt', 'r')
f = file.readlines()
test = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a""".split('\n')

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

i = 0
while i < len(f):
    line = f[i].strip().split(' ')
    if line[0] == 'cpy':
        if line[1].isdigit():
            registers[line[2]] = int(line[1])
        else:
            registers[line[2]] = registers[line[1]]
    elif line[0] == 'inc':
        registers[line[1]] += 1
    elif line[0] == 'dec':
        registers[line[1]] -= 1
    elif line[0] == 'jnz':
        if line[1].isdigit():
            value = int(line[1])
        else:
            value = registers[line[1]]
        if value != 0:
            i += int(line[2]) - 1
    i += 1

    #print(registers)

print(registers['a'])