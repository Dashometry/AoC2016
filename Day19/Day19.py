elves = []
elf_count = 1000

for i in range(elf_count):
    elves.append(i+1)

index = 0
while len(elves) > 1:
    if index + 1 == len(elves):
        elves.pop(0)
        index = 0
    else:
        elves.pop(index + 1)
        if index == len(elves) - 1:
            index = 0
        else:
            index += 1


# Everything above was only for testing cases with lower numbers to find the pattern
def get_num(a, b):
    result = 2 * (b - a) - 1
    if result > a:
        return get_num(a, result)
    return result


a = 3005290
b = 2 * a - 3
print(get_num(a, b))